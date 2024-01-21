
<img alt="casal de noivos" src="app/static/marriage/img/icons/noivos.png" style="width: 50%;">

# Casamento

Site do nosso casamento!

Link: https://henryzord.github.io/marriage

## Instalação

Usa o gerenciador de pacotes [Python Anaconda](https://www.anaconda.com/download)

```bash
conda create --name marriage python==3.12 pip --yes
conda activate marriage
pip install -r requirements.txt
```

## Execução

```bash
conda activate marriage
python app/manage.py runserver
```

## Exportar páginas HTML

Usa a biblioteca [django-bakery](https://palewi.re/docs/django-bakery/index.html)

```bash
conda activate marriage
python app/manage.py build
```
