# Use Ubuntu LTS as the base image
FROM mcr.microsoft.com/dotnet/sdk:7.0-bookworm-slim

# Install required dependencies
RUN apt update && apt install -y \
    wget \
    unzip \
    software-properties-common \
    libx11-6 \
    libxcursor1 \
    libxinerama1 \
    curl \
    libcurl4-gnutls-dev

# Include downloaded editor and os platform
COPY ./app /app

# make sure all executables have their won permissions
RUN find ./ -type f -executable -exec chmod +x {} \;

# automatically run the Editor when using this image
ENTRYPOINT [ "/app/Binaries/Editor/Linux/Release/FlaxEditor" ]
