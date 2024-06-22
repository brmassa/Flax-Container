FROM mcr.microsoft.com/dotnet/sdk:8.0-bookworm-slim

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
COPY ./app/ /flax
