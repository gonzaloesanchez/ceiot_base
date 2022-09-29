wget -O- --post-data "{\"id\":\"$1\", \"t\":\"$2\", \"h\":\"$3\"}" -H "http://localhost:8080/measurement" --header "content-type: application/json"
