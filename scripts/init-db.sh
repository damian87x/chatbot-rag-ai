#!/bin/bash

echo "🔍 Creating n8n database in PostgreSQL..."

# Create the n8n database
docker-compose exec postgres psql -U postgres -c "CREATE DATABASE n8n;"

# Verify the database was created
if [ $? -eq 0 ]; then
    echo "✅ Database 'n8n' created successfully"
    echo "🔄 Restarting n8n service to connect to the new database..."
    docker-compose restart n8n
    echo "⏳ Waiting for n8n to start up..."
    sleep 5
    echo "✅ Done! n8n should now be able to connect to the database"
    echo "🌐 Access n8n at: http://localhost:5678"
else
    echo "❌ Failed to create database. Check if PostgreSQL is running with: docker-compose ps"
fi
