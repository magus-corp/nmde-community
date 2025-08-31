# Analysis of Duplicated Services in Docker Compose Files

Consolidating duplicated services across Docker Compose files is a great way to optimize resource usage and simplify management. This often involves centralizing services like Redis or PostgreSQL.

## List of All Services and Potential Duplicates

**Redis Instances:**
*   `shared-redis` (image: `redis:latest`) - in `composes/shared-services.yaml` (New shared instance)
*   `archivist-redis` (image: `redis/redis-stack-server`) - in `composes/tubearchivist.yml` (Specialized: Redis Stack)
*   `cvat_redis_ondisk` (image: `apache/kvrocks:2.7.0`) - in `composes/cvat.yaml` (Specialized: Kvrocks, Redis-compatible)
*   ~~`cvat_redis_inmem` (image: `redis:7.2.3-alpine`) - in `composes/cvat.yaml`~~ (Consolidated into `shared-redis`)
*   ~~`redis` (image: `redis:6.2-alpine`) - in `composes/redis.yaml`~~ (Consolidated into `shared-redis`)

**PostgreSQL Instances:**
*   `shared-postgres-15` (image: `postgres:15-alpine`) - in `composes/shared-services.yaml` (For CVAT)
*   `shared-postgres-latest` (image: `postgres:latest`) - in `composes/shared-services.yaml` (Generic, formerly in `postgres.yaml`)
*   `shared-postgres-14` (image: `postgres:14-alpine`) - in `composes/shared-services.yaml` (For Typebot)
*   `librechat-pgvector` (image: `ankane/pgvector:latest`) - in `composes/shared-services.yaml` (For LibreChat, formerly `vectordb` in `librechat.yaml`)
*   ~~`cvat_db` (image: `postgres:15-alpine`) - in `composes/cvat.yaml`~~ (Consolidated to `shared-postgres-15`)
*   ~~`postgres` (image: `postgres:latest`) - in `composes/postgres.yaml`~~ (Consolidated to `shared-postgres-latest`)
*   ~~`typebot-db` (image: `postgres:14-alpine`) - in `composes/typebot.yaml`~~ (Consolidated to `shared-postgres-14`)

**MongoDB Instances:**
*   `shared-mongodb` (image: `mongo:latest`) - in `composes/shared-services.yaml` (Shared instance, now also used by LibreChat)
*   ~~`mongodb` (image: `mongo`) - in `composes/librechat.yaml`~~ (Consolidated to use `shared-mongodb`)
*   ~~`mongodb` (image: `mongo`) - in `composes/mongodb.yaml`~~ (Consolidated into `shared-mongodb`)
*   ~~`mongodb` (image: `mongo`) - in `composes/whisper.yaml` (original Whisper service)~~ (Original service removed, its MongoDB definition is gone)

**Pi-hole Instances:**
*   `pihole` (image: `pihole/pihole:latest`) - in `composes/pihole-compose.yaml` (Primary consolidated instance)
*   ~~`pihole` (image: `pihole/pihole:latest`) - in `composes/pihole.yaml`~~ (Consolidated into `pihole-compose.yaml`)

**n8n Instances:**
*   Consolidated by user. (Details of the consolidated instance are not specified here but assumed to be in one of the n8n compose files or a shared one).
*   ~~`n8n` (image: `docker.n8n.io/n8nio/n8n:ai-beta`) - in `composes/n8n-ai.yaml`~~
*   ~~`n8n` (image: `docker.n8n.io/n8nio/n8n`) - in `composes/n8n.yaml`~~

**ComfyUI Instances (similar purpose):**
*   `comfyui-docker` (image: `ghcr.io/cyntachs/comfy-webui-docker:main`) - in `composes/comfyui-neo.yaml` (Remaining instance)
*   ~~`supervisor` (image: `ghcr.io/ai-dock/comfyui:${IMAGE_TAG:-latest-jupyter}`) - in `composes/comfyui.yaml`~~ (Removed by user)

**Ollama Instances:**
*   `ollama` (image: `ollama/ollama`) - in `composes/ollama.yaml` (Primary instance, now connected to `shared_services_network`)
*   ~~`ollama` (image: `ollama/ollama`) - in `composes/typebot.yaml` (commented out)~~ (Removed)

**Other Services (single instances per file, listed for completeness):**
*   `dockge` (image: `louislam/dockge:1`) - in `composes/dockge.yaml`
*   `langflow` (image: `langflowai/langflow:latest`) - in `composes/langflow.yaml`
*   `radarr` (image: `linuxserver/radarr`) - in `composes/sonar-radar.yaml`
*   `sonarr` (image: `linuxserver/sonarr`) - in `composes/sonar-radar.yaml`
*   `jackett` (image: `linuxserver/jackett`) - in `composes/sonar-radar.yaml`
*   `deluge` (image: `linuxserver/deluge`) - in `composes/sonar-radar.yaml`
*   `jellyfin` (image: `lscr.io/linuxserver/jellyfin:latest`) - in `composes/jellyfin.yaml`
*   `game-server` (Veloren) (image: `registry.gitlab.com/veloren/veloren/server-cli:weekly`) - in `composes/veloren.yaml`
*   `watchtower` (image: `containrrr/watchtower`) - in `composes/veloren.yaml`
*   `openai-whisper-asr-webservice` (image: `onerahmet/openai-whisper-asr-webservice:latest-gpu`) - in `composes/whisper.yaml`
*   `minio` (image: `docker.io/bitnami/minio:2022`) - in `composes/minio.yaml`
*   `kasm` (image: `lscr.io/linuxserver/kasm:latest`) - in `composes/kasm-workspaces.yaml`
*   `petals` (image: `learningathome/petals:2.2`) - in `composes/mnet.yaml`
*   `kavita` (image: `jvmilazz0/kavita:latest`) - in `composes/kavita.yaml`
*   CVAT services: `cvat_server`, `cvat_worker_utils`, `cvat_worker_import`, `cvat_worker_export`, `cvat_worker_annotation`, `cvat_worker_webhooks`, `cvat_worker_quality_reports`, `cvat_worker_chunks`, `cvat_worker_consensus` (all image: `cvat/server:${CVAT_VERSION:-dev}`) - in `composes/cvat.yaml`
*   `cvat_ui` (image: `cvat/ui:${CVAT_VERSION:-dev}`) - in `composes/cvat.yaml`
*   `traefik` (image: `traefik:v3.3`) - in `composes/cvat.yaml`
*   `cvat_opa` (image: `openpolicyagent/opa:0.63.0`) - in `composes/cvat.yaml`
*   `cvat_clickhouse` (image: `clickhouse/clickhouse-server:23.11-alpine`) - in `composes/cvat.yaml`
*   `cvat_vector` (image: `timberio/vector:0.26.0-alpine`) - in `composes/cvat.yaml`
*   `cvat_grafana` (image: `grafana/grafana-oss:10.1.2`) - in `composes/cvat.yaml`
*   `kokoro-fastapi-gpu` (image: `ghcr.io/remsky/kokoro-fastapi-gpu:v0.1.4`) - in `composes/kokoro.yaml`
*   `tubearchivist` (image: `bbilly1/tubearchivist`) - in `composes/tubearchivist.yml`
*   `archivist-es` (image: `bbilly1/tubearchivist-es`) - in `composes/tubearchivist.yml`
*   `pgadmin` (image: `dpage/pgadmin4:latest`) - in `composes/pgadmin.yaml`
*   `api` (Evolution API) (image: `atendai/evolution-api:latest`) - in `composes/evolution_api.yaml`
*   `neo4j` (image: `neo4j:5.14.0`) - in `composes/neo4j.yaml`
*   `uptime-kuma` (image: `louislam/uptime-kuma:1.20.2`) - in `composes/uptime.yml`
*   `qbittorrent` (image: `lscr.io/linuxserver/qbittorrent:latest`) - in `composes/qbittorrent.yaml`
*   `motioneye` (image: `ccrisan/motioneye:master-amd64`) - in `composes/motioneye.yml`
*   `typebot-builder` (image: `maguscorp/typebot-builder:latest`) - in `composes/typebot.yaml`
*   `typebot-viewer` (image: `maguscorp/typebot-viewer:latest`) - in `composes/typebot.yaml`
*   `homepage` (image: `ghcr.io/gethomepage/homepage:latest`) - in `composes/homepage.yaml`
*   `api` (LibreChat) (image: `ghcr.io/danny-avila/librechat-dev:latest`) - in `composes/librechat.yaml`
*   `meilisearch` (LibreChat) (image: `getmeili/meilisearch:v1.7.3`) - in `composes/librechat.yaml`
*   `rag_api` (LibreChat) (image: `ghcr.io/danny-avila/librechat-rag-api-dev-lite:latest`) - in `composes/librechat.yaml`
*   `jupyter` (image: `quay.io/jupyter/pytorch-notebook:cuda12-python-3.11`) - in `composes/jn.yaml`

---

## Regarding Refactoring - Considerations

Consolidating common services like Redis and PostgreSQL is generally a good strategy. Here's a breakdown of the approach and considerations:

**General Strategy:**

1.  **Create a Shared Network:** Define a Docker network (e.g., `shared_services_network`) that all services needing shared resources will connect to.
    ```yaml
    # In a central place, or defined as external in each compose file
    networks:
      shared_services_network:
        driver: bridge
    ```
2.  **Establish Primary Service Instances:**
    *   Choose one Docker Compose file to manage the "primary" instance of each shared service (e.g., one main Redis, one main PostgreSQL). A new, dedicated `shared-infrastructure.yaml` could be ideal for this.
    *   These primary services will connect to the `shared_services_network`.
3.  **Modify Dependent Services:**
    *   In other Docker Compose files, remove the local definitions of services like Redis or PostgreSQL.
    *   Connect the applications in those files to the `shared_services_network` by declaring it as `external: true`.
        ```yaml
        services:
          my_app:
            # ...
            networks:
              - default # app-specific network
              - shared_services_network
        networks:
          default:
          shared_services_network:
            external: true
        ```
    *   Update application configurations (usually via environment variables) to point to the hostname of the shared service on the `shared_services_network` (e.g., `REDIS_HOST: primary-redis`).

**Key Considerations & Challenges:**

*   **Versioning:**
    *   **PostgreSQL:** Instances (`postgres:15-alpine`, `postgres:latest`, `postgres:14-alpine`) have been moved to `composes/shared-services.yaml` as `shared-postgres-15`, `shared-postgres-latest`, and `shared-postgres-14` respectively. This maintains version compatibility for dependent applications (CVAT, generic, Typebot) while centralizing their definitions. Each uses the `shared_services_network`.
    *   **Redis:** Generic Redis instances (`redis:6.2-alpine`, `redis:7.2.3-alpine`) have been consolidated into a `shared-redis` service using `redis:latest`. Specialized instances like `redis-stack-server` (for `archivist-redis`) and `apache/kvrocks` (for `cvat_redis_ondisk`) remain separate due to their specific feature sets or storage engine requirements.
*   **Configuration & Data:**
    *   **Databases (PostgreSQL, MongoDB):** Each application will need its own database, user, and password within the shared instance. You'll need to manage these and potentially migrate existing data from current volumes to the new shared volume.
    *   **Redis:** Applications can use different Redis DBs (0-15) or key prefixes to avoid collisions in a shared instance.
    *   **Volumes:** The primary shared service will have its data volume. Ensure this is well-managed and backed up.
*   **Application-Specific Duplicates:**
    *   **n8n:** Consolidated by user.
    *   **Typebot components:** The `typebot-builder` and `typebot-viewer` services in `composes/typebot.yaml` use `maguscorp/` prefixed images (e.g., `maguscorp/typebot-builder:latest`). This may indicate custom builds. If these are indeed custom, they cannot be simply merged or replaced with generic public images without ensuring compatibility and feature parity.
    *   **ComfyUI:** One instance (`comfyui-docker` in `composes/comfyui-neo.yaml`) remains after user removed the other.
*   **Kvrocks for CVAT:** `cvat_redis_ondisk` uses `apache/kvrocks`. While Redis-compatible, it's a different storage engine optimized for disk persistence. CVAT might be specifically architected or tested with Kvrocks. Replacing it with a standard Redis might have performance implications or require CVAT reconfiguration. It might be best to keep this separate unless you're sure CVAT works identically with your chosen shared Redis.
*   **Complexity vs. Benefit:** While consolidating saves resources, it adds interconnectedness. An issue with the shared Redis could affect many applications.
*   **Deployment:** You'll need to ensure the shared services compose file is started before others that depend on it.

**Recommendations & Path Forward:**

1.  **Prioritize:** Start with the easiest and most beneficial consolidations.
    *   **Pi-hole:** Consolidated into the instance defined in `composes/pihole-compose.yaml`. The redundant `composes/pihole.yaml` can be removed.
    *   **Redis:** Generic Redis instances have been consolidated into `shared-redis` in `composes/shared-services.yaml`. Specialized instances (Redis Stack, Kvrocks) remain separate.
2.  **Dedicated Shared Services Compose:** The `composes/shared-services.yaml` file now hosts `shared-redis` and three distinct PostgreSQL instances (`shared-postgres-15`, `shared-postgres-latest`, `shared-postgres-14`) along with the `shared_services_network`.
3.  **PostgreSQL Versioning Addressed:** Instead of merging into a single version, three separate shared PostgreSQL instances have been created in `composes/shared-services.yaml` to maintain compatibility with CVAT (`15-alpine`), Typebot (`14-alpine`), and the generic service (`latest`). Applications now connect to these via the `shared_services_network`.
    *   `composes/cvat.yaml` now points to `shared-postgres-15`.
    *   `composes/postgres.yaml` is now empty, its service moved to `shared-postgres-latest`.
    *   `composes/typebot.yaml` now relies on `shared-postgres-14` (requires `.typebot.env` update by user).
4.  **Iterative Refactoring:** Don't try to do everything at once. Refactor one service type (e.g., all basic Redis instances) across all files, test thoroughly, then move to the next.
5.  **Application-Specific Duplicates:** For services like `n8n`, `typebot` components, and `ComfyUI`, evaluate if the duplication is intentional (e.g., dev vs. prod, different feature sets, custom builds). If so, they might not be candidates for merging into a single instance, or the merge would involve standardizing on one version/build.

**Next Steps - Decisions Needed:**

Before specific `SEARCH/REPLACE` blocks can be proposed for further consolidation, decisions are needed on:

*   **MongoDB Consolidation:**
    *   MongoDB instances from `composes/mongodb.yaml` and the original `composes/whisper.yaml` have been consolidated into `shared-mongodb` in `composes/shared-services.yaml`.
    *   The `mongodb` service previously defined in `composes/librechat.yaml` has also been consolidated; LibreChat now uses `shared-mongodb`.
    *   The current `whisper.yaml` service does not use MongoDB.
*   **PostgreSQL Consolidation for LibreChat:**
    *   The `vectordb` (pgvector) service previously defined in `composes/librechat.yaml` has been moved to `composes/shared-services.yaml` as `librechat-pgvector` and uses the `shared_services_network`.
*   **Ollama Instances:** The commented-out Ollama in `typebot.yaml` has been removed. The primary instance in `composes/ollama.yaml` is now connected to the `shared_services_network`, making it accessible to Typebot if needed.

---

## Further Standardization Ideas

Beyond service consolidation, standardizing how data volumes and environment configurations are managed can further enhance the project.

### 1. Standardizing Volume Mount Paths

Currently, volume mount paths for application data and configurations are diverse across the services:
*   **Shared Services:** Now use `composes/data_shared/<service_name>_data` (e.g., for Redis, PostgreSQL, MongoDB).
*   **System-level Paths:** Some services like Pi-hole and Dockge use absolute paths like `/opt/stacks/...`.
*   **Home Directory Paths:** Services like Sonarr, Radarr, Jellyfin, and Neo4j use paths relative to the user's home directory (`~/apps_data/...`, `~/media/...`).
*   **Relative to Compose Directory:** Uptime Kuma uses `./uptime-kuma-data`.
*   **Docker Named Volumes:** Minio (`minio_data`) and CVAT (`cvat_data`, `cvat_keys`, etc.) use Docker-managed named volumes.

**Considerations & Options:**

*   **Option A: Fully Centralized Project Data Directory (e.g., `project_root/all_application_data/`)**
    *   **Structure Example:**
        *   `all_application_data/shared_services/redis/data`
        *   `all_application_data/apps/comfyui/outputs`
        *   `all_application_data/apps/jellyfin/config`
        *   `all_application_data/apps/pihole/etc-pihole`
    *   **Pros:**
        *   Single, predictable location for all persistent data, simplifying backups.
        *   Clear separation of data from the `composes/` directory.
    *   **Cons:**
        *   Can lead to very long relative paths in Docker Compose files if this central directory is far from `composes/`.
        *   Requires all services to conform, potentially disrupting established user workflows for paths like `~/media` or system-wide conventions like `/opt/stacks`.
        *   Initial migration of all existing data would be a significant effort.

*   **Option B: Standardized Relative Paths within `composes/` (e.g., `composes/app_specific_data/`)**
    *   **Structure Example:**
        *   `composes/data_shared/...` (remains for shared backend services).
        *   `composes/app_specific_data/comfyui/outputs/`
        *   `composes/app_specific_data/jellyfin/config/`
        *   `composes/app_specific_data/pihole/etc-pihole/` (would involve changing from `/opt/stacks`)
    *   **Pros:**
        *   Keeps application data relatively close to their Docker Compose definitions, making the `composes/` directory more self-contained.
        *   More consistent structure than the current mixed approach.
    *   **Cons:**
        *   The `composes/` directory itself could become very large if application data volumes are substantial.
        *   Still requires migration from external paths like `~/media` or `/opt/stacks` to achieve full consistency.

*   **Option C: Hybrid Approach with Enhanced Documentation & Gradual Refinement (Recommended Initial Path)**
    *   **Strategy:**
        *   Maintain `composes/data_shared/` for the already consolidated backend services.
        *   For individual applications, acknowledge that different strategies might be practical (e.g., `~/media` for media servers due to large data sizes and user convenience, `/opt/stacks` if it's a user's system-wide convention for such tools).
        *   **Crucially, for each service, explicitly document its data storage strategy (paths, type of volume) in `composes/README.md` under its specific section.**
        *   For new services or those where data is primarily configuration (e.g., Uptime Kuma, pgAdmin), strongly encourage or refactor to use relative paths within `composes/` (e.g., `composes/app_specific_data/<service_name>/config`).
    *   **Pros:**
        *   Balances the desire for consistency with practical considerations and user convenience.
        *   Reduces immediate disruption by allowing some existing paths to remain.
        *   Focuses on clarity through documentation.
    *   **Cons:**
        *   Less uniform than a fully centralized approach. Backup strategies would need to account for multiple locations.

### 2. Managing `.env` Files and Environment Variables

Environment variables, especially secrets, need careful handling.

**Implemented Strategy (Centralized `env_files` Directory):**
*   A new directory `composes/env_files/` has been established to store environment configuration files.
*   Services like `typebot.yaml` and `whisper.yaml` now reference their respective `.env` files from this directory (e.g., `env_file: ./env_files/typebot.env`).
*   **Example Files:** For each service requiring an `.env` file, an example file (e.g., `composes/env_files/example.typebot.env`, `composes/env_files/example.whisper.env`) is provided and tracked by Git. Users should copy these examples to their actual counterparts (e.g., `typebot.env`) and populate them with their specific values.
*   **Gitignore:** Actual `.env` files (like `composes/env_files/typebot.env`) are ignored by Git to prevent committing secrets. Example files are not ignored.
*   **Pros:**
    *   All environment configuration files are in one predictable location.
    *   Secrets are kept out of the repository by default.
    *   Example files guide users on required configurations.
*   **Cloudflare Token:** For variables like `CLOUDFLARE_TUNNEL_TOKEN` used by scripts (e.g., `composes/all_cloud`), the recommendation remains to set them in the shell environment, as documented in `composes/README.md`. An `example.cloudflare.env` file is provided for documentation purposes.
*   **Inline Variables:** For non-sensitive environment variables that are unlikely to change between deployments or users, keeping them directly in the Docker Compose files remains acceptable.

Implementing these standardizations would be an iterative process, best done service by service, with clear updates to `composes/README.md` at each step.
