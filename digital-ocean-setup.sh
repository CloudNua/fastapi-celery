# create Droplet
curl -X POST "https://api.digitalocean.com/v2/droplets" \
    -H "Authorization: Bearer $DIGITAL_OCEAN_ACCESS_TOKEN" \
    -d '{"name":"fastapi-celery-app","region":"sfo3","size":"s-2vcpu-4gb","image":"docker-18-04"}' \
    -H "Content-Type: application/json"

# check status
curl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer '$DIGITAL_OCEAN_ACCESS_TOKEN'' \
    "https://api.digitalocean.com/v2/droplets?fastapi-celery-app"
