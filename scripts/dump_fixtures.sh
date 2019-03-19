#!/bin/bash

# Dumps the important models from the heroku staging app to fixture files
# Run me from the repo root: ./scripts/dump_fixtures.sh

#app_name="staging-pyohio-website"
app_name="production-pyohio-website"

models=(
sites
sitetree
symposion_conference
symposion_sponsorship
)

for model in "${models[@]}"
do
    echo "Dumping $model..."
    heroku run --app "$app_name" python manage.py dumpdata "$model" --indent=2 -- > "fixtures/base/$model.json"
    dos2unix "fixtures/base/$model.json"
done
