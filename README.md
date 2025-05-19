# Segu

------------
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>

SELECT ?name (lo k pida)
FROM <https://data.eus/graph/people>
WHERE {
  ?person rdf:type schema:Person ;
          schema:name ?name .
}
-----------------------
PREFIX dbo: <http://dbpedia.org/ontology/>

SELECT ?animal
WHERE {
  SERVICE <https://dbpedia.org/sparql> {
    ?animal a dbo:Animal .
    }
}
LIMIT 10
---------------------------
SELECT ?s ?p ?o
WHERE {
  SERVICE <https://query.wikidata.org/sparql> {
    ?s ?p ?o .
  }
}
LIMIT 15
------------------------------
#!/bin/bash

# URL de tu instancia de GraphDB (ajusta la IP/puerto y repositorio según tu configuración)
GRAPHDB_URL="http://<TU-IP>:7200/repositories/abd-go2"

# Consulta SPARQL (del ejercicio 4)
SPARQL_QUERY='
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>

SELECT ?name
FROM <https://data.eus/graph/people>
WHERE {
  ?person rdf:type schema:Person ;
          schema:name ?name .
}
'

# Ejecutar la consulta usando curl y HTTP POST
curl -X POST \
  -H "Content-Type: application/sparql-query" \
  --data "$SPARQL_QUERY" \
  "$GRAPHDB_URL"

------------------------------
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

INSERT DATA {
  GRAPH <https://data.eus/graph/people> {
    <https://abd.eus/person/juanperez> <urn:born> "1990-05-15"^^xsd:date .
  }
}

---------------------------
INSERT DATA {
  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  PREFIX owl: <http://www.w3.org/2002/07/owl#>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX prop: <https://prop.org/>

  prop:parte_de a rdf:Property , owl:TransitiveProperty ;
                rdfs:label "parte de"@es ;
                rdfs:domain owl:Thing ;
                rdfs:range owl:Thing .
}
-----------------------------
