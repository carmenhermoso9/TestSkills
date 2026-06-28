# Solución y comentario — Reto 3

## Parte A

Si las Instructions están bien cargadas, deberías ver a Copilot explicar su razonamiento ("voy a usar X porque...") incluso en la pregunta del bucle `for`, que no toca ninguna skill — porque el SKILL.md de las skills no tiene ninguna instrucción sobre "explicar razonamiento", esa regla vive solo en `.github/copilot-instructions.md`, y las Instructions se cargan siempre, no condicionalmente.

Si **no** ves ese comportamiento en la pregunta del bucle `for`, probablemente Copilot está tratando la regla como "aplica solo cuando hay una skill de por medio" en vez de "siempre" — vale la pena anotarlo como discrepancia entre lo escrito y lo observado.

## Parte B

Con `description: Hace cosas.`, lo esperable es que la tasa de detección de la skill baje claramente o desaparezca. Si sigue detectándola perfectamente igual, puede ser que:
- El modelo esté usando otras señales (el nombre del directorio `calculadora-finanzas` sigue siendo descriptivo aunque la `description` no lo sea).
- Hayas reutilizado el mismo chat donde ya se había cargado la skill antes (revisa que sea un chat nuevo).

No olvides revertir el cambio después del experimento.

## Parte C — comparación con el ejemplo de referencia

En `ejercicios/soluciones/ejemplo-conversor-temperatura/` tienes una versión de referencia (Celsius/Fahrenheit/Kelvin). Compara tu propia skill con esta en estos puntos, no para ver "quién lo hizo mejor" sino para revisar checklist:

- ¿Tu `description` menciona explícitamente palabras que un usuario real usaría en su pregunta (no solo terminología técnica)?
- ¿Tu script devuelve siempre JSON, incluso en el caso de error? (Esto importa porque Copilot necesita poder parsear la salida de forma consistente, igual que un humano necesita un formato consistente para no tener que adivinar.)
- ¿Documentaste explícitamente qué NO cubre tu skill, como hicimos en `calculadora-finanzas` con la amortización?
- ¿El caso de error de tu script explica *por qué* es un error, no solo que lo es? (compara con el mensaje del cero absoluto en el ejemplo)

Si tu skill cubre una unidad que se solape con otra existente del repo (poco probable aquí, pero es un patrón real en proyectos grandes), prueba qué pasa cuando dos skills podrían aplicar a la misma pregunta — es un experimento extra interesante sobre cómo desambigua el agente entre varias skills candidatas.
