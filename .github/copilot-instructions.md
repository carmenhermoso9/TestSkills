# Instrucciones del proyecto TestSkills

Este repo es un entorno de pruebas para aprender Agent Skills y comportamiento de agentes. No es código de producción.

## Reglas generales

- El código de los scripts en `.github/skills/**/scripts/` debe ser Python simple, sin dependencias externas salvo las de la librería estándar, salvo que el SKILL.md correspondiente indique lo contrario.
- No modifiques los ficheros dentro de `ejercicios/soluciones/` salvo que el usuario lo pida explícitamente — son la solución de referencia y deben quedar intactas para comparar.
- Cuando ejecutes un script de una skill, antes de nada dilo en una frase: qué skill estás usando y por qué crees que aplica a la petición. Esto es pedagógico: el objetivo del repo es que el usuario vea el razonamiento, no solo el resultado.
- Si una petición del usuario no encaja claramente con ninguna skill, no fuerces su uso — explica que vas a resolverlo directamente y por qué no aplicaba ninguna skill.

## Estilo de código Python

- Type hints en funciones públicas.
- Docstrings cortas en español.
- Nombres de variables y funciones en español si el dominio es de negocio (finanzas, csv de ejemplo), en inglés si es código de infraestructura genérico.
