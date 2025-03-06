#!/bin/bash


echo "🚀 Starting ChatBot local environment..."

chmod +x init-db.sh

echo "📦 Starting all Docker services..."
docker-compose up -d

echo "⏳ Waiting for PostgreSQL to initialize..."
sleep 10

echo "🛠️ Ensuring n8n database exists..."
docker-compose exec -T postgres psql -U postgres -c "SELECT 1 FROM pg_database WHERE datname = 'n8n'" | grep -q 1 || docker-compose exec -T postgres psql -U postgres -c "CREATE DATABASE n8n;"

echo "🔄 Restarting n8n to connect to database..."
docker-compose restart n8n
echo "⏳ Waiting for n8n to start up..."
sleep 15

echo ""
echo "✅ Environment is ready!"
echo ""
echo "📋 Access your services at:"
echo "  - n8n:       http://localhost:5678"
echo ""
echo "📊 View logs:  make logs"
echo "🛑 Stop:       make down"
echo ""
