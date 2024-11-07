FROM public.ecr.aws/amazonlinux/amazonlinux:2023

RUN dnf update -y \
    && dnf install -y \
    tar \
    gzip \
    sudo \
    git \
    java \
    graphviz \
    postgresql15

COPY .devcontainer/plantuml.jar /usr/local/bin/plantuml.jar

RUN adduser ec2-user
RUN echo 'ec2-user ALL=(ALL:ALL) NOPASSWD: ALL' >> /etc/sudoers
USER ec2-user

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
RUN echo 'uv sync' >> ~/.bashrc
