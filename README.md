# 🐱 Proyecto de Gestión de Activos 🐱

¡Bienvenido al Proyecto de Gestión de Activos! Este proyecto proporciona una API para manejar información sobre laboratorios, marcas, tipos de activos y activos. 🎉

## 📋 Tabla de Contenidos

- [🚀 Instalación](#-instalación)
- [🔧 Uso](#-uso)
- [📚 Endpoints de la API](#-endpoints-de-la-api)
- [📖 Documentación](#-documentación)
- [🤝 Contribuciones](#-contribuciones)
- [📜 Licencia](#-licencia)

## 🚀 Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/coff3programing/inventarios_drf_api.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd inventarios_drf_api
    ```

3. Crea un entorno virtual:

    ```bash
    python -m venv env
    ```

4. Activa el entorno virtual:

    - En Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - En macOS y Linux:
        ```bash
        source env/bin/activate
        ```

5. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

6. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

7. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

## 🔧 Uso

Una vez que el servidor está en funcionamiento, puedes acceder a la API y a la documentación de la siguiente manera:

- 🛠 **Admin**: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- 🌐 **API**: [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)
- 📑 **Documentación Swagger**: [http://localhost:8000/docs/](http://localhost:8000/docs/)
- 📘 **Documentación Redoc**: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## 📚 Endpoints de la API

La API expone los siguientes endpoints:

- 🧪 **Laboratorios**: `/api/v1/laboratorios/`
- 🏷️ **Marcas**: `/api/v1/marcas/`
- 🏷️ **Tipo de Activos**: `/api/v1/tipoactivos/`
- 🏷️ **Activos**: `/api/v1/activos/`

### Ejemplos de uso

- Listar todos los laboratorios:
    ```http
    GET /api/v1/laboratorios/
    ```

- Crear una nueva marca:
    ```http
    POST /api/v1/marcas/
    ```

- Obtener detalles de un tipo de activo específico:
    ```http
    GET /api/v1/tipoactivos/{id}/
    ```

- Actualizar un activo existente:
    ```http
    PUT /api/v1/activos/{id}/
    ```

## 📖 Documentación

La documentación completa de la API se puede encontrar en los siguientes enlaces:

- 📑 [Documentación Swagger](http://localhost:8000/docs/)
- 📘 [Documentación Redoc](http://localhost:8000/redoc/)

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama con tu característica o arreglo de bug: `git checkout -b my-feature`
3. Realiza tus cambios y haz commit: `git commit -m 'Add some feature'`
4. Envía tus cambios a tu fork: `git push origin my-feature`
5. Crea un Pull Request.

## 📜 Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---

*Este README fue generado con amor y entusiasmo al igual que tu frontend. 🐾*
