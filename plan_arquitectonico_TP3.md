# TP3 AyED — Plan arquitectónico (sin código)

## 1. Bajada a tierra

El TP es **un programa con un menú** que arma una "casa de juegos" sobre **3 archivos binarios**.

- 4 juegos → solo **producen resultados** (ganó/perdió + créditos).
- 1 reporte → **lee** esos resultados.
- 1 administración → **ABM (alta/baja/modificación) de los datos del juego Menor-Mayor**.

La clave que te falta: **los 3 archivos NO están todos conectados con todos los juegos.**
Hay dos "mundos" casi independientes que se tocan en un solo punto (el juego Menor-Mayor).

```
   MUNDO 1: CONTENIDO DEL JUEGO                MUNDO 2: JUGADORES
   (solo lo usa Menor-Mayor)                   (lo usan los 4 juegos + Reporte)

   ┌───────────────┐   1 ───── N  ┌───────────────┐        ┌─────────────────┐
   │ Categorias.dat│──────────────│ Opciones.dat  │        │ Jugadores.dat   │
   │ (la pregunta) │  NroCategoria│ (los objetos  │        │ (nombre,        │
   │               │              │  y su valor)  │        │  créditos,      │
   └───────────────┘              └───────────────┘        │  victorias/     │
          ▲                              ▲                 │  derrotas)      │
          │ ABM                          │ Alta/Consulta   └─────────────────┘
          │                              │                         ▲
     Administración (F) ─────────────────┘                         │
                                                                   │
   Menor-Mayor (A) ── lee Categorias + Opciones ── y al final ─────┤ escribe
   Número secreto (B) ─────────────────────────────────────────────┤ escribe
   Blackjack (C) ──────────────────────────────────────────────────┤ escribe
   Par o impar (D) ────────────────────────────────────────────────┤ escribe
   Reporte (E) ────────────────────────────────────────────────────┘ solo lee
```

### Quién toca qué

| Módulo                | Categorias.dat | Opciones.dat | Jugadores.dat |
|-----------------------|:--------------:|:------------:|:-------------:|
| A. Menor-Mayor        | lee            | lee          | lee/escribe   |
| B. Número secreto     | —              | —            | lee/escribe   |
| C. Blackjack          | —              | —            | lee/escribe   |
| D. Par o impar        | —              | —            | lee/escribe   |
| E. Reporte            | —              | —            | lee           |
| F. Administración     | lee/escribe    | lee/escribe  | —             |

**Conclusión:** Jugadores.dat no sabe nada de categorías. Un jugador solo guarda *cuánto ganó/perdió en cada juego*
(la matriz 2×4) y *cuántos créditos tiene*. No hay relación entre Jugadores y Categorías.

---

## 2. Los registros, campo por campo

```
Categorias.dat                        Opciones.dat
┌───────────────────────────┐         ┌───────────────────────────┐
│ NroCategoria  int  (PK)   │◄───┐    │ NroCategoria  int  (FK)   │
│ NombreCategoria str(30)   │    └────│ NroOpcion     int         │
│ Pregunta      str(200)    │         │ objeto        str(100)    │
│ Estado        "A" / "I"   │         │ valor         int         │
└───────────────────────────┘         └───────────────────────────┘
 PK = consecutivo desde 1               Clave lógica = (NroCategoria, NroOpcion)

Jugadores.dat
┌──────────────────────────────────────────────┐
│ Nombre    str(30)   (único, sin orden)       │
│ Creditos  float     (arranca en 10.000)      │
│ Juegos    matriz 2x4 de enteros              │
└──────────────────────────────────────────────┘

 Matriz Juegos:        col 0        col 1          col 2        col 3
                    Mayor/Menor   Núm. secreto   Blackjack    Par/Impar
   fila 0 (ganó)        [ ]          [ ]           [ ]          [ ]
   fila 1 (perdió)      [ ]          [ ]           [ ]          [ ]
```

Ejemplo concreto de cómo se "enganchan" Categorias y Opciones:

```
Categorias.dat                          Opciones.dat
 1 | Edad famosos  | ¿Quién tiene más años? | A       1 | 1 | Tom Cruise    | 63
 2 | Dinero famosos| ¿Quién es más rico?    | A       1 | 2 | Messi         | 45
 3 | Países        | ¿Cuál tiene más hab.?  | I       1 | 3 | ...           | ..
                                                      2 | 1 | Messi         | 600
                                                      2 | 2 | Ronaldo       | 800
                                                      ...
 Menor-Mayor con categoría 1 → filtra Opciones donde NroCategoria == 1
```

---

## 3. Arquitectura por capas (programación modular descendente)

Regla de oro: **cada capa solo llama a la de abajo.** Los juegos NO tocan archivos directamente: usan las funciones de la capa de datos.

```
┌──────────────────────────────────────────────────────────────┐
│ CAPA 1 · PROGRAMA PRINCIPAL                                  │
│   mostrar_cartel_advertencia → menu_principal (iterativo)    │
└───────────────┬──────────────────────────────────────────────┘
                │ despacha según la opción (a..g)
┌───────────────▼──────────────────────────────────────────────┐
│ CAPA 2 · MÓDULOS FUNCIONALES (uno por opción del menú)       │
│  juego_menor_mayor │ juego_numero_secreto │ juego_blackjack  │
│  juego_par_impar   │ menu_reporte         │ menu_admin       │
│  salir (cartel final)                                        │
└───────────────┬──────────────────────────────────────────────┘
                │ usan
┌───────────────▼──────────────────────────────────────────────┐
│ CAPA 3 · SERVICIOS COMPARTIDOS DE NEGOCIO                    │
│  pedir_nombre_jugador · buscar_o_crear_jugador               │
│  actualizar_jugador (juego, gano, delta_creditos)            │
│  validar_apuesta · pedir_entero_validado · pausar/limpiar    │
└───────────────┬──────────────────────────────────────────────┘
                │ usan
┌───────────────▼──────────────────────────────────────────────┐
│ CAPA 4 · ACCESO A ARCHIVOS (acceso directo + pickle)         │
│  Jugadores:  buscar_por_nombre · leer_en_pos · grabar_en_pos │
│              · agregar_al_final · cantidad_registros         │
│  Categorias: leer_en_pos · grabar_en_pos · agregar · cantidad│
│  Opciones:   leer_en_pos · grabar_en_pos · agregar · cantidad│
└───────────────┬──────────────────────────────────────────────┘
                │
┌───────────────▼──────────────────────────────────────────────┐
│ CAPA 5 · DEFINICIÓN DE REGISTROS (clases del enunciado)      │
│  class Categoria · class Opcion · class Jugador              │
└──────────────────────────────────────────────────────────────┘
```

**Por qué conviene esto:** la lógica de "buscar jugador por nombre, crearlo si no existe, actualizar" aparece en los 4 juegos.
Se escribe **una sola vez** en la capa 3 y los 4 juegos la reutilizan. Es la parte que más puntos de consistencia te da.

---

## 4. Cómo funciona "acceso directo con pickle" (concepto)

Para poder ir **directo al registro N** sin leer todo el archivo, todos los registros deben **pesar lo mismo en bytes**.

```
archivo:  [reg 0][reg 1][reg 2][reg 3] ...
           │       │
           │       └─ posición = 1 * TAMAÑO_REGISTRO
           └─ posición = 0

 • TAMAÑO_REGISTRO = bytes que ocupa un registro serializado (se calcula una vez)
 • Para leer el reg N:       posicionarse en N * TAMAÑO → leer un registro
 • Para sobrescribir el N:   posicionarse en N * TAMAÑO → grabar
 • Cantidad de registros:    tamaño total del archivo / TAMAÑO_REGISTRO
 • Agregar uno nuevo:        posicionarse al final → grabar
```

**Consecuencia práctica importante:** los `str` tienen que tener **largo fijo** (Nombre = 30, Pregunta = 200, etc.), rellenados con espacios
antes de grabar. Si no, el tamaño serializado varía y la aritmética de posiciones se rompe.
Eso es lo que significan los "str(30)", "str(200)" del enunciado.

Al leer, lo normal es sacar los espacios sobrantes para comparar o mostrar.

---

## 5. Los juegos: flujo de cada uno

### Servicio común (los 4 juegos arrancan igual)

```
pedir nombre
    │
    ▼
recorrer Jugadores.dat buscando ese nombre (búsqueda secuencial: archivo sin orden)
    │
    ├── existe ──► guardar su posición
    └── no existe ► crear Jugador nuevo (créditos = 10.000, matriz en 0) y agregarlo al final
    │
    ▼
(juego...)
    │
    ▼
al terminar la partida: leer reg en esa posición → sumar 1 a ganó o perdió (fila 0/1, col del juego)
                        → sumar/restar créditos → regrabar en esa posición
```

### A. Menor-Mayor (el único que usa Categorias + Opciones)

```
pedir nombre ─► apuesta (≤ créditos, > 0) ─► elegir categoría ACTIVA
                                                     │
        ┌────────────────────────────────────────────┘
        ▼
  Opciones de esa categoría: mínimo 7 distintas necesarias (ver punto 9)
        │
  RONDA 1: sortear 2 opciones distintas  ──►  mostrar "1. X / 2. Y"
           jugador elige cuál tiene MAYOR valor
           mostrar valores · acierto → puntos += 1
        │
  RONDA 2: la opción CORRECTA de la ronda anterior se queda + 1 opción NUEVA sorteada
           (nunca usada antes en esta partida)
        │
  ...  hasta completar 6 rondas
        │
  puntos >= 4 → GANA (créditos += apuesta)  |  puntos < 4 → PIERDE (créditos -= apuesta)
        │
  actualizar Jugadores.dat
```

Cómo "filtrar opciones de una categoría" sin listas:

```
  1. Recorrer Opciones.dat y CONTAR cuántos registros tienen NroCategoria == elegida → N
  2. Sortear un número entre 1 y N  (random)
  3. Volver a recorrer el archivo y quedarse con el registro que es el K-ésimo de esa categoría
  4. Para evitar repetir objetos en la partida: un arreglo fijo de 6/7 enteros
     (arreglo, no lista) con los NroOpcion ya usados, y se re-sortea si salió repetido
```

### B. Número secreto

```
generar número aleatorio (rango a definir, p. ej. 1..100)  →  5 intentos
  loop mientras (intentos restantes > 0 y no adivinó):
      mostrar intentos que quedan → pedir número
      acierta → fin, mostrar en cuántos intentos
      no acierta → decir si el secreto es MAYOR o MENOR
  si se agotan → perdió, mostrar el número
actualizar Jugadores.dat (col 1)
```

### C. Blackjack (un solo mazo, sin cartas repetidas)

```
mazo = 52 cartas → arreglo de 52 marcas "ya salió / no salió" (arreglo fijo, no lista)
repartir 2 al jugador + 2 a la banca (mostrar solo 1 de la banca)

TURNO JUGADOR: mostrar cartas y total ──► ¿Pedir o Plantarse?
     Pedir  → sortear carta NO salida → recalcular
              > 21 → pierde automáticamente
              = 21 → pasa a la banca
     Plantarse → pasa a la banca

TURNO BANCA: mientras total <= 16 → pide;  >= 17 → se planta

RESULTADO: jugador pasó → gana banca | banca pasó → gana jugador
           si no: mayor puntaje gana | iguales → EMPATE (no suma ni gana ni pierde)

¿otra partida? sí → nueva partida | no → vuelve al menú
```
Un As vale 11 o 1: se cuenta como 11 y, si el total se pasa de 21, se baja a 1 (se resuelve al calcular el total).

### D. Par o impar

```
pedir nombre → si créditos == 0: "no puede jugar" y vuelve al menú
pedir apuesta (1 .. créditos) → pedir "par" o "impar"
sortear 2 dados (1..6) y sumar
coincide → créditos += apuesta, ganó | no coincide → créditos -= apuesta, perdió
actualizar Jugadores.dat (col 3)
```

---

## 6. Reporte (E)

```
submenú iterativo
 ├─ a) Jugadores por créditos (mayor → menor)
 ├─ b) Juegos jugados por un jugador
 └─ c) Volver
```

- **a)** Jugadores.dat está *sin orden* y no podés usar `sort`. Hay que **ordenar vos mismo** con un algoritmo visto en clase (burbuja / selección)
  actuando **sobre el archivo** mediante lecturas y escrituras por posición, comparando los créditos de dos registros contiguos y
  intercambiándolos. Para no alterar el archivo original podés copiarlo a uno auxiliar y ordenar la copia.
- **b)** Buscar jugador por nombre → recorrer las 4 columnas de la matriz → solo mostrar el juego si (ganó + perdió) > 0 → mostrar créditos.
  Nombre no existe → mensaje claro.

---

## 7. Administración (F)

```
pedir contraseña (oculta, 3 intentos, comparada contra una CONSTANTE)
   │ 3 fallos → "Superó los 3 intentos..." → vuelve al menú principal
   ▼
┌─ 1. Administrar Categorías ──┬─ Alta
│                              ├─ Modificación (solo el nombre)
│                              ├─ Baja (lógica)
│                              └─ Volver
├─ 2. Administrar Opciones ────┬─ Alta
│                              ├─ Consulta
│                              └─ Volver
└─ 3. Volver
```

| Operación        | Qué hace realmente |
|------------------|--------------------|
| Categoría Alta   | Pide nombre → valida que no exista (ignorando mayúsculas/minúsculas) → pide pregunta → NroCategoria = (último + 1) → Estado "A" → agrega al final |
| Categoría Modif. | Lista solo las **activas** → elige número → valida que esté en "A" → cambia nombre → regraba en su posición |
| Categoría Baja   | Lista solo las **activas** → elige número → valida "A" → cambia Estado a "I" (**baja lógica: NO se borra el registro**) |
| Opción Alta      | Si no hay categorías activas → cartel de aviso. Si hay → elegir categoría → pedir objeto + valor → NroOpcion = (cantidad de opciones de esa categoría + 1) → agrega al final |
| Opción Consulta  | Lista categorías → elige número → muestra pregunta + todos los objetos con su valor |

---

## 8. Restricciones del enunciado → qué implican en la práctica

| Restricción                                   | Traducción práctica |
|-----------------------------------------------|---------------------|
| Sin `break`, `exit()`, `while True`           | Todos los ciclos con **bandera** o condición explícita (`while not salir`, `while intentos > 0 and not acerto`) |
| `return` solo al final de una función         | **Un único return por función**, al final. Nada de returns anticipados dentro de if/for |
| Sin listas ni diccionarios                    | Solo variables sueltas, arreglos de tamaño fijo y matrices (como las del enunciado) |
| Sin `sort`, `find`, `join`                    | Ordenar y buscar con **tus propios** algoritmos |
| Archivos de acceso directo + pickle           | Registros de tamaño fijo, acceso por posición (sección 4) |
| Validaciones en cada proceso                  | Cada `input` se valida (tipo, rango, vacío) y se informa el error con un mensaje claro |
| Una función por juego como mínimo             | Ya cubierto por la capa 2 |
| Archivos en `c:\tp3\`                         | Rutas de archivos como constantes al comienzo |
| `categorias.dat` y `opciones.dat` ya existen  | Entregar con **≥3 categorías y ≥10 opciones por categoría** cargadas |

---

## 9. Ambigüedades del enunciado (conviene resolverlas con la cátedra o decidirlas y documentarlas)

1. **6 rondas necesitan 7 objetos distintos.** Cada ronda introduce 1 opción nueva y la primera usa 2. Pero el enunciado dice "mínimo 6 opciones por categoría".
   Con 6 hay que repetir objetos. En la entrega se piden 10, así que alcanza; igualmente validá en Alta/juego que la categoría tenga suficientes.
2. **¿Qué opción pasa a la siguiente ronda?** El ejemplo dice que pasa *la correcta* (Messi / Ronaldo), no la que eligió el jugador.
3. **"Mayor" o "menor"**: el ejemplo siempre usa "más". Convención simple: la respuesta correcta es **siempre la de mayor valor**,
   y las preguntas se redactan en ese sentido ("¿Quién tiene más años?"). Si dos objetos tienen igual valor, evitá el emparejamiento o re-sorteá.
4. **Apuestas en Número secreto y Blackjack:** el enunciado solo habla de apuesta para Menor-Mayor y Par/Impar,
   pero Jugadores guarda "acumulación de créditos que ganó o perdió". Decidí si apuestan todos o solo esos dos y dejalo escrito.
5. **Empate en Blackjack:** la matriz solo tiene "ganó" y "perdió", así que un empate no debería sumar a ninguna.
6. **Rango del número secreto:** no está definido.
7. **Nombres repetidos con distinta capitalización** ("Ana" vs "ana"): decidir si es el mismo jugador. (En categorías sí se pide ignorar mayúsculas.)
8. **Librerías permitidas:** el enunciado dice "no externas no permitidas". Confirmar que se pueden usar `random`, `pickle`, `os` (limpiar pantalla / existencia de archivos)
   y `getpass`/`msvcrt` (contraseña oculta).

---

## 10. Orden de construcción recomendado

```
PASO 1  Clases de registros (Categoria, Opcion, Jugador)
PASO 2  Capa de archivos: crear/leer/grabar/agregar/contar para los 3 archivos  ← probar con datos de prueba
PASO 3  Administración (F): Categorías Alta → Opciones Alta → Consulta → Modif. → Baja
        (así cargás los datos mínimos exigidos: 3 categorías × 10 opciones)
PASO 4  Servicios de Jugador: buscar_o_crear + actualizar
PASO 5  Par o impar (el más simple: valida todo el circuito de Jugadores + créditos)
PASO 6  Número secreto
PASO 7  Menor-Mayor (usa todo lo anterior)
PASO 8  Blackjack (el más largo en reglas)
PASO 9  Reporte (incluye el ordenamiento propio)
PASO 10 Menú principal + cartel de advertencia + cartel de salida
PASO 11 Pasada final: sin break/exit/while True, un return por función, validaciones, mensajes claros
```

Criterio del orden: primero lo que **todos** necesitan (archivos), después lo más simple que valida el circuito completo (Par/Impar),
y recién después los juegos con más reglas.
