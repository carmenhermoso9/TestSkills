# Solución y comentario — Reto 6

## Ejercicio A

Comportamiento esperado (no garantizado): la `description` de `calculadora-prestamos` menciona explícitamente "hipotecas" y "cuotas mensuales", que son justo los términos más distintivos de tu pregunta — más distintivos que la frase genérica "interés compuesto" que mencionas de pasada. Si el agente pesa bien la semántica completa de la pregunta (no solo la primera palabra clave que encuentra), debería elegir `calculadora-prestamos` y devolver:

```json
{
  "principal": 200000.0,
  "tasa_anual": 0.03,
  "anios": 20,
  "cuota_mensual": 1109.2,
  "total_pagado": 266206.85,
  "total_intereses": 66206.85
}
```

Si en cambio Copilot elige `calculadora-finanzas` y fuerza ese script con `--aportacion-anual` tratando la cuota como una aportación que suma (en vez de un pago que amortiza), el resultado es matemáticamente incorrecto y sin aviso — exactamente el fallo silencioso que ya anticipamos en el Reto 1. Si te pasa esto, es información valiosa: significa que la palabra "interés compuesto" en tu prompt pesó más que el contexto semántico completo de "hipoteca con cuotas".

## Ejercicio B

No hay un "correcto" objetivo aquí — es un ejercicio de observación. Casuísticas posibles:
1. Copilot asume que es una inversión (usa `calculadora-finanzas`) porque tu frase no menciona ninguna cuota ni pago periódico, y el patrón "tengo X€, qué pasa en Y años" se parece más a "capital que crece" que a "deuda que amortizo".
2. Copilot pregunta explícitamente antes de elegir.

Si pasa lo (1), es razonable — la ausencia de cualquier mención a "cuota" o "pago mensual" es información real a favor de la interpretación de inversión. Anota cuál fue, y si te parece la interpretación más sensata dada la frase, no necesariamente un fallo.

## Ejercicio C

Comportamiento esperado: al decir explícitamente "no estoy segura si es préstamo o inversión", le estás quitando al agente la posibilidad de "adivinar con seguridad" — debería preguntarte directamente cuál es la situación antes de ejecutar nada, porque tú misma señalizaste la ambigüedad en vez de dejarla implícita.

Si Copilot ejecuta una de las dos skills igualmente sin preguntar, vale la pena anotarlo como un caso de "el agente prefiere actuar a preguntar" incluso cuando el usuario pidió explícitamente lo contrario — un patrón de comportamiento real que conviene conocer si vas a delegar tareas más serias en el futuro (conecta con "Riesgo: perder el control del código" de tu propio mapa).

## Reflexión

El patrón general observable en estos 3 ejercicios suele ser: cuanto más explícita es la ambigüedad en tu prompt (B vs C), más probable es que el agente pregunte en vez de asumir. Y cuantos más términos distintivos y no solapados tenga la `description` de cada skill, menos depende el agente de la suerte para desambiguar correctamente. Esto es, otra vez, la misma lección del Reto 3 Parte B aplicada en un contexto distinto: la calidad de la `description` no solo importa para decidir "¿aplica esta skill sí o no?", sino también para decidir "¿cuál de estas dos skills aplica mejor?".
