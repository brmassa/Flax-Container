# Flax Engine Containers

[Flax engine](https://flaxengine.com) inside the a container to be used in CI/CD of your games. Build your games automatically in the cloud!

> It's a non-official project.

A sample project is in https://gitlab.com/brmassa/flax-container-sample-project, which uses GitLab CI/CD.

The base image is the standard [.NET SDK](https://hub.docker.com/_/microsoft-dotnet-sdk/) image, which is based on Debian.

## Usage

Depends on what is your remote repository and CI/CD pipeline. It uses the standard [Flax terminal commands](https://docs.flaxengine.com/manual/editor/advanced/command-line-access.html) to generate the build.

### GitLab

If you have your code in a GitLab instance, just create a `.gitlab-ci.yml` file in the app/game folder with the content:

```yaml
build:
  image: registry.gitlab.com/brmassa/flax-container:1.7.6407.2-linux_amd64
  stage: build
  script:
    - /flax/Binaries/Editor/Linux/Release/FlaxEditor -project ./ -std -null -headless -build "Release.Linux_x64"
    - mv Output/Linux_x64 MyApp       # rename the output file to the final desired name
  artifacts:
    paths:
      - MyApp                         # It will automatically create a Zip file with this folder
```

### GitHub

WIP #3

## Issues

### **Windows** builds fail

I will investigate why Flax fails to build. #1

### **Android** builds fail

WIP. The Android image still do not install the Android SDK, so it will fail.  #2
