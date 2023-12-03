#!/bin/sh

if [ ! -f /app/.env ]; then 
    echo "Copying .env.example to .env..."
    cp /app/.env.example /app/.env
fi

if [ ! -d /app/database/data ]; then 
    echo "Creating postgres data directory..."
    mkdir -p /app/database/data
fi

if [ ! -d /app/database/pgadmin_data ]; then 
    echo "Creating pgadmin data directory..."
    mkdir -p /app/database/pgadmin_data
fi

if [ ! -d /app/notebook/agent_workspace ]; then 
    echo "Creating agent workspace..."
    mkdir -p /app/notebook/agent_workspace
fi

echo "Initialization complete."
