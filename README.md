# Flax Engine Containers

Build and deploy your [Flax Engine](https://flaxengine.com) games automatically in the cloud using containerized CI/CD pipelines!

> **Note**: This is a non-official project and is not affiliated with Flax.

## Overview

This project provides Docker containers with Flax Engine pre-installed, enabling seamless integration into CI/CD workflows for game development. Build your games automatically in the cloud across multiple platforms!

A sample project demonstrating usage with GitLab CI/CD is available at: https://gitlab.com/brmassa/flax-container-sample-project

## Base Image

The containers are built on top of the official [.NET SDK](https://hub.docker.com/_/microsoft-dotnet-sdk/) image, which is based on Debian.

## Supported Platforms

- Linux (AMD64)
- Windows (AMD64)
- Android (ARM64)
- Xbox One
- Windows Store

## Usage

The containers utilize standard [Flax terminal commands](https://docs.flaxengine.com/manual/editor/advanced/command-line-access.html) for building games. Integration depends on your specific CI/CD pipeline and remote repository.

### GitLab CI/CD

To use with GitLab CI/CD, create a `.gitlab-ci.yml` file in your project's root directory:

```yaml
build:
  image: registry.gitlab.com/brmassa/flax-container:linux_amd64-latest  # Or use a fixed version like flax-container:linux_amd64-1.7.6407.2
  stage: build
  script:
    - /flax/Binaries/Editor/Linux/Release/FlaxEditor -project ./ -std -null -headless -build "Release.Linux_x64"
    - mv Output/Linux_x64 MyApp  # Rename the output folder
  artifacts:
    paths:
      - MyApp  # GitLab CI will automatically create a zip file with this folder
```

### GitHub Actions

Support for GitHub Actions is in progress. See issue #3 for updates.

## Known Issues

### Windows Builds Failing

There's an ongoing investigation into Windows build failures. For updates, please refer to issue #1.

### Android Builds Failing

Android builds are currently not functional as the Android SDK is not yet installed in the image. This is being addressed in issue #2.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Acknowledgments

- [Flax Engine](https://flaxengine.com) - The game engine that powers this project
- [.NET SDK](https://hub.docker.com/_/microsoft-dotnet-sdk/) - The base image for our containers

For any questions or support, please open an issue in the GitHub repository.
