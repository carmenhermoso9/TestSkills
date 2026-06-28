# Solución y comentario — Reto 1

## Ejercicio A

Comportamiento esperado:
- Copilot debería identificar `calculadora-finanzas` por la descripción ("interés compuesto", "crecimiento de una inversión") y construir:
  ```bash
  python3 .github/skills/calculadora-finanzas/scripts/interes_compuesto.py --capital 5000 --tasa 0.04 --anios 8
  ```
- Resultado esperado del script: saldo final ≈ **6841.49 €**.
- Punto clave a observar: el LLM **no calcula el interés compuesto él mismo** — delega en el script. Si alguna vez ves que Copilot te da un número sin pasar por el terminal, es señal de que decidió no usar la skill y calculó "a ojo" con el LLM, lo cual es justo el comportamiento no determinista que tu mapa describe (mismo prompt, podría no usar siempre la skill).

## Ejercicio B

Comando esperado:
```bash
python3 .github/skills/calculadora-finanzas/scripts/interes_compuesto.py --capital 2000 --tasa 0.03 --objetivo-multiplicador 2
```
Resultado: **24 años** (puedes verificarlo tú con `1.03^24 ≈ 2.03`).

Si Copilot en cambio usa `--anios` con algún valor arbitrario, es un fallo de mapeo prompt→argumento — vale la pena anotarlo como ejemplo real de "el agente interpretó mal la intención" para tu propio aprendizaje.

## Ejercicio C

Este es el más interesante. El SKILL.md dice explícitamente: *"No uses esta skill para préstamos con cuotas (amortización)"*. Comportamientos posibles que puedes observar:

1. **Comportamiento correcto:** Copilot lee la skill, ve que no aplica, te explica que esto es amortización con cuotas y no interés compuesto simple, y o bien lo resuelve con una fórmula distinta explicada en texto, o te dice que necesitarías otra skill/script para eso.
2. **Comportamiento subóptimo:** fuerza el script con `--aportacion-anual` tratando la cuota como si fuera una aportación que *suma* en vez de una amortización que *resta* deuda — el resultado sería matemáticamente incorrecto y, si Copilot no te avisa, es un fallo silencioso real.

Si te ocurre el caso 2, es un ejemplo perfecto para tu aprendizaje: demuestra por qué las skills deben documentar explícitamente sus límites, no solo su alcance positivo — exactamente lo que ya hiciste bien en el SKILL.md que te dimos.

## Reflexión sobre `description` vaga

Si la cambias a "Hace cosas", lo normal es que Copilot deje de asociarla con preguntas de interés compuesto, o dude entre resolverlo él mismo con el LLM vs buscar una skill. Esto es la prueba empírica de que el *discovery* de skills depende casi enteramente de la calidad semántica de `description` — no hay ninguna otra señal previa que el agente tenga para decidir.
