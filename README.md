
<img alt="casal de noivos" src="app/static/img/icons/noivos.png" style="width: 40%;">

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

### Para executar o servidor Django

```bash
conda activate marriage
python app/manage.py runserver
```

### Para exportar páginas para HTML

Usa a biblioteca [django-bakery](https://palewi.re/docs/django-bakery/index.html). Só funciona no Linux!

```bash
conda activate marriage
python app/manage.py build
```

### Para converter imagens png/jpg para webp

```bash
conda activate marriage
python convert_images.py --path app/static/img/icons
```

## Workflows

A workflow [django.yml](.github/workflows/django.yml) renderiza as páginas HTML estáticas, move para a pasta
[docs](/docs), e publica no GitHub Pages automaticamente.