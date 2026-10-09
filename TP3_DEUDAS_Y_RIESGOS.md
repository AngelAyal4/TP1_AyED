# TP3 — Deudas técnicas y riesgos

Notas pendientes de la integración de `categoriasOC.py` + `OpcionesCategorias0C.py` en `tp3/TP3_Final.py`.
Fecha: 2026-10-08

---

## Deudas (decisiones tomadas, pendientes de resolver)

### Deuda 1 — Validación del menú con lista
El menú principal valida la opción con una **lista literal**:

```python
while opcion not in ["A", "B", "C", "D", "E", "F", "G"]:
```

El enunciado (§Notas) prohíbe usar listas: *"NO usar listas ni diccionarios ni ninguna otra estructura de datos que no se haya dado en el curso."*
Se dejó así por decisión del equipo. **Fix pendiente** (1 línea): comparar por rango de letras, ya que A–G son contiguas:

```python
while len(opcion) != 1 or opcion < "A" or opcion > "G":
```

Forma parte de la pasada final de cumplimiento (PASO 11 del plan arquitectónico).

### Deuda 2 — Archivos `.dat` en mayúsculas vacíos
En `tp3/` conviven archivos vacíos con mayúscula inicial:

- `Categorias.dat`
- `Opciones.dat`
- `Jugadores.dat`

El programa usa los de minúscula (`categorias.dat`, `opciones.dat`, `jugadores.dat`).
- En **Linux** son archivos distintos → los mayúsculos son basura inofensiva.
- En **Windows** (`c:\tp3\`) el sistema de archivos es case-insensitive → "Categorias.dat" y "categorias.dat" son **el mismo archivo**. No rompe, pero conviene dejar un solo nombre para evitar confusión.

**Fix pendiente:** borrar los 3 archivos vacíos en mayúscula antes de la entrega.

### Deuda 3 (resuelta) — Datos iniciales para la entrega
El enunciado (§2, "Importante") exige que **`categorias.dat` y `opciones.dat` ya existan** en la entrega con **al menos 3 categorías y 10 opciones por categoría**.
**Estado:** `categorias.dat` tiene **6 categorías activas** y `opciones.dat` **60 opciones (10 por categoría)**, cargadas por el menú de Alta (F → Administración de Juegos). Cumple de sobra el mínimo.
- El seed automático (`cargarCategoriasIniciales`/`cargarOpcionesIniciales`) queda como **red de seguridad** si los `.dat` se borran (carga 3 categorías × 3 opciones); los archivos de entrega ya están completos.

---

## Riesgos / limitaciones conocidas

### Riesgo 1 — Tamaño de registro y enteros
El acceso directo asume registros de tamaño fijo. `pickle` codifica los `int` chicos (0–255) en 1 byte y los más grandes en más bytes.
- `NroCategoria`: mientras sea < 256, el registro de categoría mide siempre igual (OK). Con 256+ categorías cambiaría de tamaño. **No aplica a este TP.**
- `valor` de opciones: es un `int` arbitrario y cambia de tamaño al serializarse. **No rompe nada** porque Opciones **nunca usa acceso directo** (solo barridos secuenciales y append al final).

### Riesgo 2 — Acentos y tamaño de registro
`formatear()` usa `sinAcentos()` + `.ljust()`. Se normalizan los textos a ASCII para que cada campo ocupe siempre la misma cantidad de **bytes** (los acentos en UTF-8 ocupan 2 bytes y desalineaban el acceso directo).
Consecuencia: los textos se guardan/muestran **sin acentos** (ej. `"Países"` → `"Paises"`, `"¿Quién...?"` → `"?Quien...?"`).
**Pendiente:** consultar a la cátedra si esto es aceptable o si prefieren otra estrategia (ver consulta enviada al profesor).

### Riesgo 3 — Juegos sin implementar (A y E implementados)
El menú principal ya tiene las opciones A–G, pero:
- `A` (Mayor/Menor): **implementado** — apuesta, 6 rondas (la correcta pasa de ronda), ≥4/6 gana, actualiza créditos y la matriz (col 0). Usa `random` y un arreglo fijo `[0]*8` para no repetir objetos.
- `B`, `C`, `D`: muestran "en construcción" (stub).
- `E` (Reporte): **implementado** (a: jugadores por créditos; b: juegos de un jugador).

Se portan de los TP anteriores en fases siguientes. Los stubs evitan el `NameError` que crasheaba el programa.

**Decisión Mayor/Menor:** el orden en que se muestran las 2 opciones de cada ronda se **randomiza** (`random.randint(0,1)`). Si no, la opción correcta que pasa de ronda quedaría siempre en la posición 1 y el juego sería trivial (bastaría responder siempre "1"). El enunciado pide opciones "aleatorias"; el ejemplo del enunciado es ambiguo con las etiquetas (1/2 luego 2/3).

### Riesgo 5 — CRUD de Jugadores: alcance
Implementado: `buscarJugador` (R), `crearJugador` (C), `mostrarJugador` (R), `actualizarJugador` (U), `ordenarJugadoresPorCreditos` y `reportePartidasJugador`.
- No hay **baja** de jugadores: el enunciado no la pide (los jugadores se actualizan, no se eliminan).
- `mostrarJugador` y `actualizarJugador` son funciones de servicio: las usarán los juegos al terminar cada partida. `actualizarJugador` todavía no tiene menú que la exponga.
- El ordenamiento por créditos se hace sobre una **copia auxiliar** (`jugadores_aux.dat`) para no alterar el orden del archivo original (que es "sin ningún orden" según el enunciado).
- `tamanioRegistroJugador` asume los contadores de la matriz 2×4 < 256 (mismo límite que `NroCategoria`).

### Riesgo 6 (resuelto) — Jugadores: búsqueda secuencial, sin orden
Se probó el patrón de `libretaContactos.py` (alta → burbuja por nombre → búsqueda dicotómica) sobre `jugadores.dat`, pero **se revirtió**.
- **Motivo:** el enunciado (§2, línea 45) rotula `Jugadores.dat` como *"(sin ningún orden)"*; mantenerlo ordenado por nombre contradice esa descripción.
- **Estado final:** `buscarJugador` = **secuencial**; `crearJugador` = solo alta al final; `ordenarJugadoresPorNombre` eliminada.
- Si la cátedra pide dicotómica en algún lado, el patrón queda documentado acá para reimplementarlo.
- Nota: el Reporte a) sigue ordenando por créditos sobre la **copia auxiliar** (`jugadores_aux.dat`), que es un criterio distinto y no toca el orden del máster.

### Riesgo 4 — Edición concurrente (VSC)
Si el archivo se edita desde el editor y desde el agente a la vez, el buffer viejo de VSC puede **pisar** los cambios (ya pasó: apareció una función duplicada).
**Recomendación:** antes de guardar en VSC hacer `Ctrl+Shift+P` → **File: Revert File**, y no editar en paralelo.

---

## Convenciones de código

### Declaración de globales (estilo `libretaContactos.py`)
Cada función que toca un handle de archivo (`arLoCategorias`, `arLoOpciones`, `arLoJugadores`, `arLoJugadoresAux`) lo declara con `global` al comienzo, siguiendo la convención del ejemplo de la cátedra.
- **Obligatorio** (Python lo exige) solo donde la función **asigna** la variable: `abrirArchivos` y `copiarJugadoresAux`.
- En el resto (funciones que solo **leen** el handle) es **redundante pero intencional**: auto-documenta que la función opera sobre el archivo global y evita el bug de crear una variable local por error si alguien agrega una asignación.
- Las rutas `RUTA_CATEGORIAS`/`RUTA_OPCIONES`/`RUTA_JUGADORES` son **constantes** (nunca se reasignan) → **no** llevan `global`. Diferencia respecto de la referencia, que usa `arFi*` mutables; acá el plan arquitectónico pide rutas como constantes al comienzo.

## Estado actual

- `tp3/TP3_Final.py`: integración de CRUD Categorías + Opciones + Jugadores (R/U), Administración (§F), Reporte (§E) y menú A–G.
- `tp3/categoriasOC.py` y `tp3/OpcionesCategorias0C.py`: módulos de prueba standalone (se mantienen).
- `tp3/categorias.dat` y `tp3/opciones.dat`: **6 categorías activas** + **60 opciones (10 por categoría)**, cargadas vía el menú de Alta. Listas para el juego Menor-Mayor.
