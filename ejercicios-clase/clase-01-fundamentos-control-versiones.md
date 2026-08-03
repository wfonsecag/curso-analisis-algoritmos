# Clase 01: Fundamentos de control de versiones y flujo de trabajo

## Idea principal

El control de versiones resuelve el problema de trabajar sobre archivos que cambian con el tiempo sin perder el historial de lo que se hizo, cuándo se hizo y por qué se hizo.

## Problemas que resuelve Git

- Evita depender de nombres como `final`, `final_v2` o `YA_arreglado`.
- Permite volver a un punto anterior cuando un cambio rompe algo.
- Ayuda a combinar el trabajo de varias personas sin copiar y pegar archivos a mano.
- Hace posible revisar el historial completo del proyecto.

## Conceptos clave

### Terminal

La terminal es la ventana de texto donde se escriben los comandos. En esta clase se usaron conceptos básicos como:

- `pwd` para ver la carpeta actual.
- `ls` o `dir` para listar contenido.
- `cd` para moverse entre carpetas.
- `mkdir` para crear carpetas.
- `clear` o `cls` para limpiar la pantalla.

### Repositorio

Un repositorio es una carpeta cuya historia de cambios queda guardada por Git. Al ejecutar `git init` se crea la carpeta oculta `.git/`, donde vive ese historial.

### `.gitignore`

Sirve para decirle a Git qué archivos o carpetas no debe rastrear, por ejemplo:

- `__pycache__/`
- `*.pyc`
- `.vscode/`
- archivos temporales o de resultados

### `README.md`

Es la carta de presentación del proyecto. Debe explicar de qué trata el repositorio, cómo está organizado y cómo se usa.

### Staging area y commit

Git separa el trabajo en dos pasos:

1. `git add` prepara los cambios.
2. `git commit` guarda una foto permanente de esos cambios en el historial.

### `HEAD`

`HEAD` indica en qué commit estás parado actualmente, normalmente el último commit de tu rama activa.

### `git diff`

Permite ver el cambio exacto entre archivos antes de hacer commit.

## Comandos más importantes

```bash
git init
git status
git add <archivo>
git commit -m "mensaje"
git log --oneline
git diff
```

## Repositorios remotos

Git puede sincronizar un repositorio local con GitHub. Los comandos más importantes son:

- `git clone`: descargar un repositorio por primera vez.
- `git push`: subir cambios al remoto.
- `git fetch`: traer cambios sin aplicarlos.
- `git pull`: traer y aplicar cambios de una vez.

## Colaboradores

En GitHub, un colaborador es una cuenta a la que se le da permiso para hacer `push` y `pull` en el repositorio.

## Ramas

Las ramas permiten probar cambios en paralelo sin afectar `main` hasta que todo esté listo.

Comandos vistos:

```bash
git branch
git checkout <rama>
git checkout -b <nueva-rama>
git merge <rama>
```

## Conflictos de fusión

Un conflicto aparece cuando dos cambios modifican la misma parte de un archivo y Git no puede combinarlos automáticamente. Se resuelve editando el archivo a mano y eliminando los delimitadores del conflicto.

## Resumen final

Git sirve para guardar memoria del proyecto, revisar cambios, colaborar con otras personas y trabajar con seguridad sobre el historial del código.
