FROM postgres:16

COPY scripts/*.sql /docker-entrypoint-initdb.d/

HEALTHCHECK --interval=10s --timeout=5s --start-period=3s --retries=5 CMD pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}
