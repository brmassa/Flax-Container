# Dockerfile
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env

WORKDIR /app

# Download and unzip files
RUN apt-get update && apt-get install -y wget unzip libx11-6 libxcursor1 libxinerama1 curl libcurl4-gnutls-dev glibc libstdc++6

RUN wget https://vps2.flaxengine.com/store/builds/Package_1_06_06344/FlaxEditorLinux.zip
RUN unzip -o FlaxEditorLinux.zip -d /app && rm FlaxEditorLinux.zip

RUN wget https://vps2.flaxengine.com/store/builds/Package_1_06_06344/Linux.zip
RUN unzip -o Linux.zip -d /app && rm Linux.zip

RUN find ./ -type f -executable -exec chmod +x {} \;
