# API books via FastAPI
## How to use
### Make container
```bash
docker build -t books:latest .
docker run -p 8000:8000 [img_id]:[tag]
```
or
```bash
docker-compose up --build
```
Document for api
```
http://localhost:8000/docs
```