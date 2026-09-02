# Estructura del Proyecto — TP1_AyED

Suite de juegos de azar y lógica en Python, desarrollado para la materia
**Algoritmos y Estructura de Datos** (UTN — Comisión 1º K13).

---

## 1. Árbol de archivos

```text
TP1_AyED/
│
├── AyED_TP2_2026.pdf          # Enunciado oficial de la materia
├── ARCHITECTURE.md            # Esta guía de arquitectura
├── README.md                  # Instrucciones de uso y contenido del proyecto
│
├── Juego_Principal.py         # ★ APLICACIÓN PRINCIPAL ★
│                              #   - Menú iterativo
│                              #   - 4 juegos + módulo de reportes
│                              #   - Variables globales compartidas
│                              #   - Funciones de búsqueda y ordenamiento
│
├── juego_dados.py             # Módulo auxiliar (juego de dados standalone)
│                              #   - Referencia histórica; no integra globals
│
├── juego-b.py                 # Prototipo de Blackjack (etapa inicial)
│
├── TP1-game-1.py              # Prototipo de la primera entrega (temas básicos)
│
├── Juego_Principal copy.py    # Copia de respaldo del principal (snapshot)
│
├── Cosas que cambie para el   # Notas de cambios pendientes (Angel)
│   commit.txt                 #   (archivo de trabajo, no entregar)
│
└── __pycache__/               # Compilados de Python (generado automáticamente,
│                              #   ignorado por git)
```

---

## 2. Arquitectura de Juego_Principal.py

### 2.1 Variables globales (sección inicial)

```text
┌────────────────────────────────────────────────────────────────────┐
│                    VARIABLES GLOBALES                              │
│                                                                    │
│  MAX_JUGADORES = 10  (constante, cupo máximo por juego)           │
│                                                                    │
│  ┌─────────────────────────────┐   ┌─────────────────────────────┐│
│  │  MAYOR O MENOR              │   │  NÚMERO SECRETO             ││
│  │  mm_nombre_ultimo_jugador  │   │  ns_nombre_ultimo_jugador  ││
│  │  mm_nombres[10]  (str)     │   │  ns_nombres[10]  (str)     ││
│  │  mm_rachas[10]   (int)     │   │  ns_jugadas[10]  (int)     ││
│  │  mm_cantidad_jugadores (int)│  │  ns_ganadas[10]  (int)     ││
│  └─────────────────────────────┘   │  ns_perdidas[10] (int)     ││
│                                     │  ns_cantidad_jugadores    ││
│                                     └─────────────────────────────┘│
│  ┌─────────────────────────────┐   ┌─────────────────────────────┐│
│  │  BLACKJACK                  │   │  PAR O IMPAR                ││
│  │  bj_nombre_ultimo_jugador  │   │  pi_nombre_ultimo_jugador  ││
│  │  bj_jugadores[10]  (str)   │   │  pi_nombres[10]   (str)    ││
│  │  bj_jugadas[10]    (int)   │   │  pi_jugadas[10]   (int)    ││
│  │  bj_ganadas[10]    (int)   │   │  pi_ganadas[10]   (int)    ││
│  │  bj_perdidas[10]   (int)   │   │  pi_perdidas[10]  (int)    ││
│  │  bj_empatadas[10]  (int)   │   │  pi_creditos[10]  (int)    ││
│  │  bj_cantidad_jugadores     │   │  pi_cantidad_jugadores     ││
│  └─────────────────────────────┘   └─────────────────────────────┘│
└────────────────────────────────────────────────────────────────────┘
```

### 2.2 Flujo de ejecución (main)

```text
                    ┌──────────────┐
                    │  PROGRAMA    │
                    │    INICIA    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ mostrar_     │
                    │ advertencia() │  ← Cartel ASCII de advertencia
                    └──────┬───────┘     (requiere Enter para continuar)
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                         main()                                │
│                                                              │
│   ┌──────────────────────────────────────────────────────┐   │
│   │  MOSTRAR MENÚ (iterativo, hasta que opción == "S")   │   │
│   │                                                      │   │
│   │  A → juego_mayor_menor()                             │   │
│   │  B → juego_numero_secreto()                          │   │
│   │  C → juego_blackjack()                               │   │
│   │  D → juego_par_o_impar()                             │   │
│   │  E → reporte()                                       │   │
│   │  S → imprimir despedida + salir                      │   │
│   └──────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
```

---

## 3. Módulos y sus algoritmos

### 3.1 `buscar_jugador(nombres, cantidad, nombre_buscado)`

```text
ALGORITMO: BÚSQUEDA SECUENCIAL

     índice = 0
     posicion = -1

     mientras índice < cantidad_y_posicion == -1:
         si nombres[indice].lower() == nombre_buscado.lower():
             posicion = índice          # ← encuentro, detiene búsqueda
         sino:
             índice = índice + 1        # ← avanza al siguiente

     retornar posicion                   # ← -1 si no encontró
```

- Recorre el arreglo de nombres posición por posición.
- Comparación insensible a mayúsculas/minúsculas (`.lower()` es permittedo).
- Sin `break`, sin `return` intermedio (la versión original usaba `return` dentro del loop — corregido).
- Retorna el índice del jugador o `-1` si no existe.

---

### 3.2 `juego_mayor_menor()`

```text
Juego "Mayor o Menor"

Estrategia:
  1. Solicitar nombre (validación sin break: while con bandera)
  2. Buscar jugador existente / registrar nuevo
  3. Generar número de referencia aleatorio (randint 1..1000)
  4. Loop principal:
       - Mostrar referencia
       - Pedir "mayor" o "menor" (validar entrada)
       - Generar nuevo número aleatorio
       - Comparar y actualizar racha o finalizar
  5. Mostrar GAME OVER con racha obtenida
```

Algoritmos internos:
- Generación de números aleatorios: **randint()** (permitido)
- Validación de entrada: comparación de strings con `.strip().lower()` (permitido)

---

### 3.3 `juego_numero_secreto()`

```text
Juego "Número Secreto"

Estrategia:
  1. Solicitar nombre (validación sin break)
  2. Buscar / registrar jugador
  3. Generar número secreto (randint 1..100)
  4. Loop de intentos (máximo 6):
       - Mostrar intentos restantes
       - Pedir número:
         * validar que sea string no-vacío
         * validar dígitos carácter por carácter con while indexado
         * convertir a entero con función manual (sin int())
         * validar rango 1..100
       - Comparar con número secreto (mayor/menor/igual)
       - Contar intento
  5. Mostrar resultado final + actualizar estadísticas
```

Algoritmos internos:
- **Conversión manual de dígitos a entero** — `convertir_digitos_a_entero(texto)`:
  - Recorre el string con slice `texto[indice:indice+1]` hasta obtener `""`
  - Cada caracter se compara contra `'0'`..`'9'` con `if/elif` para obtener su valor
  - Construye el número: `resultado = resultado * 10 + valor`
  - Sin `int()`, sin `ord()`, sin `len()`, sin `for()`

---

### 3.4 `juego_blackjack()`

```text
Juego "Blackjack — El 21"

Estrategia:
  1. Solicitar nombre (validación sin break)
  2. Buscar / registrar jugador
  3. Loop de partidas (mientras bj_jugar_otra == "S"):
       a) Construir mazo de 52 cartas:
          - BJ_PALOS = ["♠","♥","♦","♣"]  (arreglo de strings)
          - BJ_RANGOS = ["2".."10","J","Q","K","A"]  (arreglo de strings)
          - Carta = [rango, palo]  ← LISTA de 2 strings, no tupla
            (los arreglos solo contienen un tipo: aquí strings)
       b) Barajar mazo — Fisher-Yates manual (sin shuffle()):
          - Desde i = 51 hasta i > 0:
            j = randint(0, i)
            intercambiar mazo[i] ↔ mazo[j]
            i = i - 1
       c) Repartir 2 cartas a jugador y 2 a banca
       d) Mostrar manos y puntos (bj_calcular_puntos)
       e) Si blackjack natural → resolver inmediatamente
       f) Si no → turno del jugador (pedir/plantarse):
          - "Pedir": repartir carta, recalcular puntos
            * si >21 → pierde
            * si ==21 → turno a banca
          - "Plantarse": fin del turno del jugador
       g) Turno de la banca (mientras puntos <= 16, pedir carta)
       h) Determinar ganador:
          - banca >21 → gana jugador
          - jugador > banca → gana jugador
          - jugador < banca → pierde jugador
          - iguales → empate (salvo blackjack natural de banca)
       i) Actualizar estadísticas
       j) Preguntar si quiere otra partida
  4. Volver al menú
```

Algoritmos internos:
- **Fisher-Yates** — barajado uniforme sin `random.shuffle()`
- **bj_calcular_puntos(cartas, cantidad)** — sumar valores, ajustar ases:
  - As = 11 inicial; si total >21 y hay ases, restar 10 por cada uno
  - J/Q/K = 10; números del 2 al 10 = su valor
  - Conversión de rango a valor: `convertir_digitos_a_entero(bj_rango)` (sin `int()`)
- Cartas representadas como **listas** `[rango, palo]` (no tuplas, cumpliendo regla de un solo tipo por arreglo)

---

### 3.5 `juego_par_o_impar()`

```text
Juego "Par o Impar" (Dados)

Estrategia:
  1. Solicitar nombre (validación sin break)
  2. Buscar / registrar jugador (crédito inicial = $1000)
  3. Loop de rondas (mientras crédito > 0 y juego_activo):
       a) Mostrar crédito disponible
       b) Pedir apuesta:
          - validar dígitos con while indexado (sin isdigit())
          - convertir con función manual (sin int())
          - validar monto > 0 y <= crédito
       c) Pedir paridad (1=Par, 2=Impar)
       d) Tirar 2 dados (randint 1..6), sumar
       e) Determinar paridad de la suma
       f) Comparar con apuesta del jugador:
          - acierto → sumar apuesta al crédito, contar ganada
          - fallo → restar apuesta al crédito, contar perdida
       g) Mostrar resultado y estadísticas
       h) Preguntar si continúa (1=seguir, 2=salir)
  4. Si crédito == 0 → mensaje y fin del juego
```

---

### 3.6 Reportes

```text
Módulo de reportes (submenú iterativo dentro de reporte())

  A → reporte_jugadores_por_victorias()
      Por cada juego (NS, BJ, PI):
        → reporte_mostrar_jugadores_ordenados(nombres, victorias, cant, título, True)
        (orden descendente por victorias)

  B → reporte_juegos_por_jugador()
      Pedir nombre → buscar en los 4 arreglos → mostrar stats de cada juego

  C → reporte_creditos_par_impar()
      → reporte_ordenar_indices(pi_creditos, cant, False)
      (orden ascendente por crédito)

  D → reporte_racha_mayor_menor()
      Pedir nombre → buscar en mm_nombres → mostrar racha

  E → volver al menú principal
```

#### `reporte_ordenar_indices(valores, cantidad, descendente)`

```text
ALGORITMO: ORDENAMIENTO POR SELECCIÓN (sobre arreglo de índices)

     indices = [0, 1, 2, ... cantidad-1]   ← arreglo auxiliar

     para posición desde 0 hasta cantidad-2:
         posicion_elegida = posición
         comparación = posición + 1

         mientras comparación < cantidad:
             valor_comparado = valores[indices[comparación]]
             valor_elegido   = valores[indices[posicion_elegida]]

             si descendente:
                 si valor_comparado > valor_elegido:
                     posicion_elegida = comparación
             sino (ascendente):
                 si valor_comparado < valor_elegido:
                     posicion_elegida = comparación

             comparación = comparación + 1

         intercambiar indices[posición] ↔ indices[posicion_elegida]
         posición = posición + 1

     retornar indices
```

- No modifica el arreglo original de valores.
- Trabaja sobre un arreglo de índices que referencia los valores.
- Complejidad O(n²), adecuado para n ≤ 10 jugadores.

---

## 4. Restricciones implementadas

| Constructo              | Estado  | Sustitución aplicada                          |
|-------------------------|---------|-----------------------------------------------|
| `break`                 | ❌ NO   | While con bandera booleana                    |
| `continue`              | ❌ NO   | No utilizado                                   |
| `len()`                 | ❌ NO   | No necesario (slicing hasta cadena vacía)     |
| `append()`              | ❌ NO   | Arreglos pre-dimensionados de tamaño 10       |
| `shuffle()`             | ❌ NO   | Fisher-Yates manual con `randint()`           |
| `isdigit()`             | ❌ NO   | Recorrido char-by-char con `while` indexado   |
| `int()`                 | ❌ NO   | `convertir_digitos_a_entero()` manual         |
| `return` dentro de loop | ❌ NO   | Reemplazado por variable de resultado + loop  |
| Tuplas `(a, b)`         | ❌ NO   | Listas `[a, b]` (un solo tipo por arreglo)   |
| `.lower()` / `.upper()` | ✅ SI   | Solo donde está permitido (comparaciones)     |
| `.strip()`              | ✅ SI   | Limpieza de entrada de usuario                |
| `random.randint()`      | ✅ SI   | Generación de números aleatorios              |

---

## 5. Autores del grupo

| Nombre                     | Rol                          |
|----------------------------|------------------------------|
| Angel Jose Ayala           | Desarrollo principal         |
| Gabriela Iglesias          | Member                       |
| Maximiliano Iván Campos    | Member                       |
| Santiago Nicolás Bolzan    | Revision y correcciones      |

---

## 6. Entregas

| Entrega | Temas cubiertos                              | Estado     |
|---------|----------------------------------------------|------------|
| TP1     | Variables, bucles, condicionales (temas básicos) | Prototipo en `TP1-game-1.py` |
| TP2     | Arreglos + funciones (esta entrega)         | `Juego_Principal.py` actual |
| TP3     | Enunciado pendiente — aún no disponible      | Por definir |

---

*Generado para la defensa del trabajo práctico — UTN Comisión 1º K13.*
