FROM ubuntu:22.04

# Set non-interactive mode during build
ENV DEBIAN_FRONTEND=noninteractive

# Update and install essential packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create symbolic link for python
RUN ln -sf /usr/bin/python3 /usr/bin/python

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Set working directory
WORKDIR /app

# Set up an alias in the bashrc to run your script easily
RUN echo 'alias fl-ids="python3 /app/src/main.py"' >> /root/.bashrc

# Install Python packages from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Command to run when the container starts
CMD ["bash"]