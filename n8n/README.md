# n8n Integration Guide

[n8n](https://n8n.io/) is a workflow automation platform included in this project. This guide explains how to work with n8n in the context of this project.

## Overview

n8n allows you to create automated workflows using a visual editor. It connects APIs, services, and applications through a node-based workflow system.

## Getting Started

1. Start all services using Docker Compose:
   ```
   docker-compose up -d
   ```

2. Access the n8n editor in your browser:
   ```
   http://localhost:5678
   ```

3. The default credentials are:
   - Email: `admin@example.com`
   - Password: `password`
   (Change these in production environments)

## Integrating with Job Agent

To integrate n8n with the job agent service:

1. Use HTTP Request nodes to connect to the job agent API at `http://job_agent:3000`
2. Create workflows that trigger on job events
3. Process and transform job data using n8n nodes

### Example Workflow: Job Processing

1. Create a new workflow in n8n
2. Add a "Webhook" trigger node to receive job submissions
3. Add a "HTTP Request" node to send data to the job agent
4. Add a "Function" node to transform the response
5. Add notification nodes (Email, Slack, etc.) as needed

## Custom Nodes

You can extend n8n with custom nodes:

1. Create a new directory in `n8n/custom-nodes/`
2. Implement your custom node following the n8n [documentation](https://docs.n8n.io/integrations/creating-nodes/)
3. Add your custom node to the Docker setup

## Environment Variables

n8n configuration is controlled through environment variables in `docker-compose.yml`. Key variables:

- `N8N_PORT`: The port n8n runs on (default: 5678)
- `N8N_PROTOCOL`: HTTP or HTTPS
- `N8N_HOST`: Hostname for n8n
- `DB_TYPE`: Database type (PostgreSQL in this setup)
- `DB_POSTGRESDB_*`: PostgreSQL connection details

## Persistent Data

n8n data is stored in:
- PostgreSQL database for workflows and credentials
- Docker volume (`n8n_data`) for user files

## Security Considerations

- Change default credentials in production
- Set up HTTPS for production deployments
- Secure sensitive credentials in the n8n credentials store
- Consider implementing [encryption](https://docs.n8n.io/hosting/environment-variables/encryption/)

## Troubleshooting

- Check Docker logs: `docker-compose logs n8n`
- Verify database connection: `docker-compose logs postgres`
- Ensure ports are not in use by other applications
- Check n8n container health: `docker ps | grep n8n`
