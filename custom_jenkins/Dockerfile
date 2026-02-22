# Use Jenkins LTS
FROM jenkins/jenkins:lts

USER root

# Install required packages
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker’s official GPG key (modern method)
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | \
    gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg

# Add Docker repository (MATCH bookworm!)
RUN echo \
  "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bookworm stable" \
  > /etc/apt/sources.list.d/docker.list

# Install only Docker CLI
RUN apt-get update && \
    apt-get install -y docker-ce-cli && \
    apt-get clean

# Add Jenkins user to docker group
RUN groupadd -f docker && \
    usermod -aG docker jenkins

USER jenkins