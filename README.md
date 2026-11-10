# Trabajo Integrador - EcoTech Solutions

Repositorio organizado en tres carpetas, una por ejercicio.

```
ejercicio1/   Sanitización y análisis estadístico de sensores
ejercicio2/   Modelo de productos, excepciones y persistencia JSON
ejercicio3/   Auditoría con tests unitarios e integración web (proyecto Django)
```

## Ejercicio 1

```bash
cd ejercicio1
python ejercicio1.py
```

## Ejercicio 2

```bash
cd ejercicio2
python ejercicio2.py
```

Genera el archivo `catalogo_ecotech.json` en la misma carpeta.

## Ejercicio 3 (Django)

```bash
cd ejercicio3

# crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # Linux / Mac python3 
venv\Scripts\activate           # Windows

# instalar dependencias
pip install -r requirements.txt

# correr los tests unitarios
python manage.py test sustentabilidad

# levantar el servidor
python manage.py migrate
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/sustentabilidad/

### Archivos principales

- `sustentabilidad/services.py`: `calcular_emisiones_carbono` y `obtener_metricas_consumo`
- `sustentabilidad/tests.py`: clase `TestCalculoEmisiones(unittest.TestCase)`
- `sustentabilidad/views.py`: vista `vista_panel_sustentabilidad(request)`
- `sustentabilidad/templates/sustentabilidad/panel.html`: plantilla del panel
