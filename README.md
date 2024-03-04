# Sport-App-Metricas
Repositorio para el servicio Metricas, se desea utilizar kubernetes y ci - cd con aws


## ejecución local
```python
flask --app src/api run -p 3000
```

## ejecución producción
```python
gunicorn src.api:app --bind 0.0.0.0:3000
```

## ejecución por docker
```python
docker build -t metrics-service .
docker run --env-file ./.env -p 3000:3000 metrics-service
```