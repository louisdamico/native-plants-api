#!/bin/bash

curl "http://localhost:8000/mangos" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
