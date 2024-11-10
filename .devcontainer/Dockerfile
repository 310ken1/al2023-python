FROM public.ecr.aws/amazonlinux/amazonlinux:2023

# パッケージインストール
RUN --mount=type=cache,target=/var/cache/dnf \
    dnf update -y \
    && dnf install -y \
    tar \
    gzip \
    sudo \
    git \
    java \
    graphviz \
    ipa-gothic-fonts \
    postgresql15

# PlantUMLインストール
ARG plantuml="https://github.com/plantuml/plantuml/releases/download/v1.2024.7/plantuml-1.2024.7.jar"
RUN curl -LsSf ${plantuml} -o /usr/local/bin/plantuml.jar

# ユーザ追加
ARG user="ec2-user"
RUN adduser ${user}
RUN echo "${user} ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers
USER ${user}
WORKDIR /home/${user}

# 依存関係（パッケージ）のインストール
# https://docs.astral.sh/uv/guides/integration/docker/#developing-in-a-container
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy
RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable

