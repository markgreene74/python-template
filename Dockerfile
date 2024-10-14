# syntax=docker/dockerfile:1

# base
FROM python:3.12-slim-bookworm AS base
ARG POETRY_VERSION="1.8.3"
RUN adduser --disabled-login --gecos "" user
USER user
ENV PATH="${PATH}:/home/user/.local/bin/"
WORKDIR /usr/src/app
ENV POETRY_VERSION=${POETRY_VERSION}
RUN pip install --upgrade setuptools pip && \
    pip install --upgrade poetry==${POETRY_VERSION}
COPY --chown=user:user application application/
COPY --chown=user:user data data/
COPY --chown=user:user poetry.lock pyproject.toml ./

# test
FROM base AS test
USER user
ENV PATH="${PATH}:/home/user/.local/bin/"
WORKDIR /usr/src/app
RUN poetry install --with test --no-root
ENV PYTHONPATH="${PYTHONPATH}:/user/src/app"
COPY --chown=user:user test test/
# make sure pytest will use color in terminal output
ENV FORCE_COLOR="true"
CMD ["poetry", "run", "pytest"]

# dev
FROM test AS dev
USER root
RUN apt-get update && \
    apt-get install git vim -y
USER user
ENV PATH="${PATH}:/home/user/.local/bin/"
WORKDIR /usr/src/app
COPY --chown=user:user .gitignore .pre-commit-config.yaml ./
RUN poetry install --with test,dev --no-root
RUN git init . && \
    poetry run pre-commit --version && \
    poetry run pre-commit install
ENV PYTHONPATH="${PYTHONPATH}:/user/src/app"
CMD ["/bin/bash"]

# run
FROM base AS run
USER user
ENV PATH="${PATH}:/home/user/.local/bin/"
WORKDIR /usr/src/app
RUN poetry install --only main --no-root
ENV PYTHONPATH="${PYTHONPATH}:/user/src/app"
CMD ["poetry", "run", "python", "application/main.py"]
