# Use Ubuntu LTS as the base image
FROM mcr.microsoft.com/dotnet/sdk:7.0-bookworm-slim

# Download and unzip files

## Engine (the Linux version)
ARG ENGINE_URL
RUN wget $ENGINE_URL -O engine.zip
RUN unzip -o engine.zip -d /app && rm engine.zip

## Platform Tools
ARG OS_PLATAFORM_URL
RUN wget $OS_PLATAFORM_URL -O package.zip
RUN unzip -o Lipackagenux.zip -d /app && rm package.zip

RUN find ./ -type f -executable -exec chmod +x {} \;
ENTRYPOINT [ "/app/Binaries/Editor/Linux/Release/FlaxEditor" ]

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