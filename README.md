# flask-template

## Development

```bash
flask --app src/app --debug run --host=0.0.0.0 --port=8080
```

## Production

```bash
python src/app.py
```

## Docker

```bash
docker build -f Dockerfile -t flask-template:latest ./
```

## Others

### Generate requirements.txt

```bash
pip install pipreqs -i https://pypi.tuna.tsinghua.edu.cn/simple
pipreqs ./ --force
```