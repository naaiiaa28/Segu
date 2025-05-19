#!/bin/bash

# Variables (la ip del servidor y el abd-01 es el nombre del repositorio de graph)
ENDPOINT_URL="http://35.187.117.15:7200/repositories/abd-01"
##consulta del sparql.05
SPARQL_QUERY='
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?g ?s ?p ?o
WHERE {
  ?g dcat:theme "museos" .
  GRAPH ?g {
    ?s rdf:type foaf:person .
    ?s foaf:name "Aitor Labajo" .

    ?s ?p ?o .

  }
}

'

# Ejecutar consulta SPARQL vía POST
curl -X POST "$ENDPOINT_URL" \
     -H "Content-Type: application/sparql-query" \
     -H "Accept: application/sparql-results+json" \
     --data "$SPARQL_QUERY"
