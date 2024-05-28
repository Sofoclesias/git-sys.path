# Añade el directorio raíz de git al entorno virtual de tus notebooks.

Estoy harto de que los notebooks solo te detecten el directorio local donde se ubican para sus labores. Particularmente, me tiene hastiado que no respeten los entornos virtuales creados por los repositorios para organizar los proyectos.

Este repositorio, de forma sencilla y directa, agrega un comando al archivo de configuraciones de IPython para que agregue al sys.path el directorio que contenga la carpeta .git, es decir, el directorio raíz de un repositorio. Así, ya tendrás la libertad para manipular todos los archivos relativos a tu repositorio en el kernel de Notebook e importar todos tus módulos.

Por ejemplo, si tienes un diseño de directorios así:

/repositorio
    /.git
    /folder
        notebook.ipynb
    utils.py

Tomando como referencia el directorio donde se ubique el Notebook, se explorarán los directorios padres hasta encontrar aquél que contenga el folder .git, a lo que se agregará al sys.path.
