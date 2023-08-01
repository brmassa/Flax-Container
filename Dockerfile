# Use Ubuntu LTS as the base image
FROM ubuntu:22.04

# Import repository keys
RUN apt-get update && apt-get install -y gnupg2
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 871920D1991BC93C

# Install required dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    software-properties-common \
    libx11-6 \
    libxcursor1 \
    libxinerama1 \
    curl \
    libcurl4-gnutls-dev

# Install .NET SDK 7.0
RUN wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && add-apt-repository universe \
    && apt-get update \
    && apt-get install -y apt-transport-https \
    && apt-get update \
    && apt-get install -y dotnet-sdk-7.0

# Download and unzip files
RUN wget https://vps2.flaxengine.com/store/builds/Package_1_06_06344/FlaxEditorLinux.zip
RUN unzip -o FlaxEditorLinux.zip -d /app && rm FlaxEditorLinux.zip

RUN wget https://vps2.flaxengine.com/store/builds/Package_1_06_06344/Linux.zip
RUN unzip -o Linux.zip -d /app && rm Linux.zip

RUN find ./ -type f -executable -exec chmod +x {} \;
