# flask-template

## Development

```bash
flask --app src/app --debug run
```

## Production

```bash
python src/app.py
```

## Generate requirements.txt

```bash
pip install pipreqs -i https://pypi.tuna.tsinghua.edu.cn/simple
pipreqs ./ --force
```