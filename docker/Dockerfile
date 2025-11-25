FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock ./

# Copy code and tests
COPY src/ ./src/
COPY tests/ ./tests/

# Install dependencies using uv
RUN uv sync --frozen --no-dev

# Set up entrypoint for tests
CMD ["uv", "run", "pytest", "tests/", "-v"]
