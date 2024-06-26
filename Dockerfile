FROM mcr.microsoft.com/dotnet/sdk:8.0-noble

# Install required dependencies
RUN apt update && apt install -y \
    build-essential \
    curl \
    libcurl4-gnutls-dev \
    libx11-6 \
    libxcursor1 \
    libxinerama1 \
    software-properties-common \
    unzip \
    wget

# Include downloaded editor and os platform
COPY ./app/ /flax
