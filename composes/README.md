# Docker Compose Configurations

This directory contains a collection of `docker-compose.yaml` files for various applications and services. These configurations allow for easy deployment and management of containerized environments within the Magic Desktop Environment (MDE).

## Structure

*   **`*.yaml` files**: Each `.yaml` file represents a distinct Docker Compose application or service stack.
*   **`env_files/`**: This subdirectory contains example `.env` files corresponding to the Docker Compose configurations. These files are used to manage environment variables, sensitive information, and customizable settings for each service.

## Usage

To deploy a service using its Docker Compose file:

1.  **Navigate to the `composes` directory:**
    ```bash
    cd /home/magus/.config/mde/composes
    ```
2.  **Copy and configure the environment file:**
    Before running a compose file, you should copy its corresponding example environment file from `env_files/` and customize it with your specific settings. For example:
    ```bash
    cp env_files/example.my_service.env ./.my_service.env
    # Then, edit ./.my_service.env with your preferred editor
    ```
    **Note**: Ensure that the `.env` file is named correctly (e.g., `.my_service.env` for `my_service.yaml`) or referenced explicitly in your `docker-compose.yaml` if it deviates from the default naming convention.

3.  **Start the service:**
    ```bash
    docker compose -f <service_name>.yaml up -d
    ```
    Replace `<service_name>.yaml` with the actual filename (e.g., `jellyfin.yaml`). The `-d` flag runs the services in detached mode.

4.  **Stop the service:**
    ```bash
    docker compose -f <service_name>.yaml down
    ```

5.  **View logs:**
    ```bash
    docker compose -f <service_name>.yaml logs -f
    ```

## Available Services

Each `.yaml` file in this directory corresponds to a specific application. Refer to the individual `docker-compose.yaml` files and their respective `example.*.env` files for detailed configuration options and service descriptions.

---

*These Docker Compose configurations are designed to provide a flexible and reproducible way to run various applications within the MDE.*