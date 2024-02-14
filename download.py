import os
import json
import urllib.request
import zipfile

PLATFORM_MAP = {
    "linux_amd64": "Linux (target platform)",
    "windows_amd64": "Windows (target platform)",
    "android_arm64": "Android (target platform)",
    "xboxone": "Xbox One (target platform)",
    "windows_store": "Windows Store (target platform)"
}

def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def unzip_file(zip_file, extract_path):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def delete_file(filename):
    os.remove(filename)

def main():
    # Download JSON
    json_url = "https://api.flaxengine.com/launcher/engine"
    with urllib.request.urlopen(json_url) as response:
        data = json.loads(response.read())

    # Get FLAX_VERSION and PLATFORM from environment or arguments
    flax_version = os.getenv("FLAX_VERSION") or "1.7"  # Default version
    platform_env = os.getenv("OS_PLATFORM") or "windows_adm64"  # Default platform
    platform = PLATFORM_MAP.get(platform_env)

    print(f"Using FLAX_VERSION: {flax_version}")
    print(f"Using PLATFORM: {platform}")
    if not platform:
        print("Invalid platform environment variable.")
        return

    # Find the version data
    version_data = next((v for v in data["versions"] if v["version"] == flax_version), None)
    if version_data:
        # Find the package URLs based on platform
        editor_url = next((p["url"] for p in version_data["packages"] if p["name"] == "Editor"), None)
        platform_package = next((p["url"] for p in version_data["packages"] if p["name"] == platform), None)

        if editor_url and platform_package:
            # Download Editor and platform package
            print(f"Downloading Editor: {editor_url}")
            download_file(editor_url, "Editor.zip")
            print(f"Downloading Platform tool: : {platform_package}")
            download_file(platform_package["url"], f"{platform}.zip")

            # Unzip files
            print("Extracting Editor.")
            unzip_file("Editor.zip", ".")
            print("Extracting Platform tool.")
            unzip_file(f"{platform}.zip", platform)

            # Delete zip files
            delete_file("Editor.zip")
            delete_file(f"{platform}.zip")
            print("Download and extraction completed.")
        else:
            print("Editor or platform package not found for the specified version and platform.")
    else:
        print("Version not found in the JSON data.")

if __name__ == "__main__":
    main()
