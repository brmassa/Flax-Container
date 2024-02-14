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

# Download and unzip files

## Engine (the Linux version)
# ARG ENGINE_URL
# RUN wget $ENGINE_URL -O engine.zip
# RUN unzip -o engine.zip -d /app && rm engine.zip

# ## Platform Tools
# ARG OS_PLATFORM_URL
# RUN wget $OS_PLATFORM_URL -O platform.zip
# RUN unzip -o platform.zip -d /app && rm platform.zip

RUN find ./ -type f -executable -exec chmod +x {} \;
ENTRYPOINT [ "/app/Binaries/Editor/Linux/Release/FlaxEditor" ]
