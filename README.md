# casamento

Site do nosso casamento!

## Instalação

```bash
conda create --name marriage pip --yes
conda activate marriage
pip install -r requirements.txt
```

## Execução

```bash
conda activate marriage
python app/manage.py runserver
```

## Exportar páginas HTML

```bash
conda activate marriage
python app/manage.py distill-local docs
```
