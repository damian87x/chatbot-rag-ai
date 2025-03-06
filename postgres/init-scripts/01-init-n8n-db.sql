-- Create n8n database
CREATE DATABASE n8n;

-- Connect to the n8n database
\c n8n

-- Grant privileges to the postgres user
GRANT ALL PRIVILEGES ON DATABASE n8n TO postgres;

-- Log creation
\echo '=== n8n database initialized successfully ==='
