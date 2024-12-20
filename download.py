import os
import json
import urllib.request
import zipfile

PLATFORM_MAP = {
    "linux_amd64": {
        "name": "Linux (target platform)",
        "editor_zip": "/FlaxEditorLinux.zip"
    },
    "windows_amd64": {
        "name": "Windows (target platform)",
        "editor_zip": None                      # The default Editor.zip is Windows
    },
    "android_arm64": {
        "name": "Android (target platform)",
        "editor_zip": "/FlaxEditorLinux.zip"
    },
    "xboxone": {
        "name": "Xbox One (target platform)",
        "editor_zip": None
    },
    "windows_store": {
        "name": "Windows Store (target platform)",
        "editor_zip": None
    }
}

def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)


def replace_editor_zip(url, platform):
  if platform['editor_zip'] is None:
    return url
  parsed_url = urllib.parse.urlparse(url)
  new_path = parsed_url.path.replace("/Editor.zip", platform['editor_zip'])
  return urllib.parse.urlunparse((parsed_url.scheme, parsed_url.netloc, new_path, parsed_url.params, parsed_url.query, parsed_url.fragment))

def unzip_file(zip_file, extract_path):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def delete_file(filename):
    os.remove(filename)

def set_permission_executables(path):
    for root, _, files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.isfile(filepath) and not os.access(filepath, os.X_OK):
                os.chmod(filepath, os.stat(filepath).st_mode | 0o111)
                print(f"Make it executable: {filepath}")

def set_environment_variables(version_data):
    flax_version_full = version_data["version"]
    print(f"Using FLAX_VERSION_FULL:\t{flax_version_full}")
    # os.environ['FLAX_VERSION_FULL'] = flax_version_full
    with open('_env', 'w') as writer:
        writer.write(f'export FLAX_VERSION_FULL={flax_version_full}')
    github_env_file = os.getenv('GITHUB_ENV')
    if github_env_file and os.access(github_env_file, os.W_OK):
        with open(github_env_file, 'a') as writer:
            writer.write(f'FLAX_VERSION_FULL={flax_version_full}')

def main():
    # Download JSON
    json_url = "https://api.flaxengine.com/launcher/engine"
    with urllib.request.urlopen(json_url) as response:
        data = json.loads(response.read())

    # Get FLAX_VERSION and PLATFORM from environment or arguments
    flax_version = os.getenv("FLAX_VERSION") or "1.9"               # Default version
    platform_env = os.getenv("OS_PLATFORM")  or "windows_amd64"     # Default platform
    platform = PLATFORM_MAP.get(platform_env)

    print(f"Using FLAX_VERSION:\t\t{flax_version}")
    print(f"Using OS_PLATFORM:\t\t{platform['name']}")
    if not platform:
        print("Invalid platform environment variable.")
        return

    # Find the version data
    version_data = next((v for v in data["versions"] if v["name"] == flax_version), None)
    if version_data:
        set_environment_variables(version_data)
        # Find the package URLs based on platform
        editor_url = next((p["url"] for p in version_data["packages"] if p["name"] == "Editor"), None)
        editor_url = replace_editor_zip(editor_url, platform)
        os_platform_url = next((p["url"] for p in version_data["packages"] if p["name"] == platform['name']), None)

        if editor_url and os_platform_url:
            # Download Editor and platform package
            print(f"Downloading Editor:\t\t{editor_url}")
            download_file(editor_url, "Editor.zip")
            print(f"Downloading OS Platform tool:\t{os_platform_url}")
            download_file(os_platform_url, f"{platform_env}.zip")

            # Unzip files
            print("Extracting Editor.")
            unzip_file("Editor.zip", "./app")

            print("Extracting OS Platform tool.")
            platform_mini = platform_env.split('_')[0].capitalize()
            unzip_file(f"{platform_env}.zip", f"./app/Source/Platforms/{platform_mini}/")

            set_permission_executables("./app")

            print("Download and extraction completed.")
        else:
            print("Editor or platform package not found for the specified version and platform.")
    else:
        print("Version not found in the JSON data.")

if __name__ == "__main__":
    main()
