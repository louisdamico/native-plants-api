#!/bin/bash

curl "http://localhost:8000/mangos/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
