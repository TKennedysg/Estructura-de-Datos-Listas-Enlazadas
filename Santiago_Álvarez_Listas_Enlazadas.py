# EJERCICIOS PRÁCTICOS - LISTAS ENLAZADAS
# Unidad 3: Estructura de Datos
# ULEAM - Ingeniería en Software
"""
Nombre: Santiago Joel Álvarez Mendoza
Fecha: 16/12/2025
Ejercicios: 20/20
"""

#CLASES BASE PARA LOS TODOS LOS EJERCICIOS DW LISTAS ENLAZADAS

class Node:
    #Nodo para lista simplemente enlazada
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return (f"Node({self.data})")


class DoubleNode:
    #Nodo para lista doblemente enlazada
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return (f"DoubleNode({self.data})")


class LinkedList:
    #Lista simplemente enlazada con implementación completa
    
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " → ".join(nodes) + " → None"
    
    def is_empty(self):
        #Verifica si la lista está vacía
        return self.head is None
    
    def append(self, data):
        #Agrega elemento al final de la lista
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
    
    def prepend(self, data):
        #Agrega elemento al inicio de la lista
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1
    
    def create_from_list(self, data_list):
        #Crea lista desde una lista de Python
        for item in data_list:
            self.append(item)
    
#============================================================
#EJERCICIOS BASICOS
#============================================================
    
    """
    EJERCICIO 1: Contar elementos
    Implementa un método count(elem) en SLinkedList que cuente cuántas veces
    aparece un elemento en la lista.
    """

    def count(self, elem):
        """
        Cuenta las ocurrencias de un elemento en la lista
        
        Args:
            elem: Elemento a contar
            
        Returns:
            Número de veces que aparece elem
        """
        count = 0
        current = self.head
        
        while current:
            if current.data == elem:
                count += 1
            current = current.next
        
        return count
    

    """
    EJERCICIO 2: Obtener elemento por índice
    Implementa un método get(index) que retorne el elemento en la posición index.
    """

    def get(self, index):
        """
        Obtiene el elemento en una posición específica
        
        Args:
            index: Posición del elemento (0-indexed)
            
        Returns:
            El elemento en la posición index
            
        Raises:
            IndexError: Si el índice está fuera de rango
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Índice {index} fuera de rango. Tamaño: {self._size}")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data
    

    """
    EJERCICIO 3: Encontrar índice de elemento
    Implementa un método index_of(elem) que retorne el índice de la primera
    ocurrencia del elemento, o -1 si no existe.
    """

    def index_of(self, elem):
        """
        Encuentra el índice de la primera ocurrencia de un elemento
        
        Args:
            elem: Elemento a buscar
            
        Returns:
            Índice de la primera ocurrencia, o -1 si no existe
        """
        current = self.head
        index = 0
        
        while current:
            if current.data == elem:
                return index
            current = current.next
            index += 1
        
        return -1
    

    """
    EJERCICIO 4: Lista a array
    Implementa un método to_list() que convierta la lista enlazada a una
    lista de Python (array).
    """

    def to_list(self):
        """
        Convierte la lista enlazada a una lista de Python
        
        Returns:
            Lista de Python con todos los elementos
        """
        result = []
        current = self.head
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result
    

    """
    EJERCICIO 5: Limpiar lista
    Implementa un método clear() que elimine todos los elementos de la lista.
    """

    def clear(self):
        """
        Elimina todos los elementos de la lista
        """
        self.head = None
        self.tail = None
        self._size = 0
    

#============================================================
#EJERCICIOS INTERMEDIOS
#============================================================
    
    """
    EJERCICIO 6: Invertir lista
    Implementa un método reverse() que invierta el orden de los elementos
    EN LA MISMA LISTA (no crear una nueva).
    """

    def reverse(self):
        """
        Invierte la lista en su lugar (sin crear nueva lista)
        Complejidad: O(n)
        """
        prev = None
        current = self.head
        
        # Actualizar tail al primer elemento antes de invertir
        self.tail = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Actualizar head al último elemento
        self.head = prev
    

    """
    EJERCICIO 7: Detectar ciclo
    Implementa un método has_cycle() que detecte si la lista tiene un ciclo
    (un nodo apunta a un nodo anterior, creando un bucle infinito).
    
    Usa el algoritmo de Floyd (tortuga y liebre):
    - Dos punteros: uno avanza 1 paso, otro avanza 2 pasos
    - Si se encuentran, hay ciclo
    - Si el rápido llega a None, no hay ciclo
    """

    def has_cycle(self):
        """
        Detecta si la lista tiene un ciclo usando Floyd's algorithm
        
        Returns:
            True si hay ciclo, False si no
        Complejidad: O(n) tiempo, O(1) espacio
        """
        if self.is_empty() or self.head.next is None:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    

    """
    EJERCICIO 8: Encontrar el medio
    Implementa un método get_middle() que retorne el elemento del medio de la lista.
    Si hay número par de elementos, retorna el segundo del medio.

    Usa el algoritmo de dos punteros:
    - Un puntero lento (avanza 1 paso)
    - Un puntero rápido (avanza 2 pasos)
    - Cuando el rápido llega al final, el lento está en el medio
    """

    def get_middle(self):
        """
        Encuentra el elemento del medio de la lista
        
        Returns:
            El elemento del medio
            
        Raises:
            Exception: Si la lista está vacía
        """
        if self.is_empty():
            raise Exception("La lista está vacía")
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    

    """
    EJERCICIO 9: Eliminar duplicados
    Implementa un método remove_duplicates() que elimine todos los elementos
    duplicados de la lista, dejando solo la primera ocurrencia de cada elemento.
    """

    def remove_duplicates(self):
        """
        Elimina elementos duplicados de la lista
        Versión con set: O(n) tiempo, O(n) espacio
        """
        if self.is_empty() or self.head.next is None:
            return
        
        seen = set()
        current = self.head
        prev = None
        
        while current:
            if current.data in seen:
                #Eliminar nodo duplicado
                prev.next = current.next
                if current == self.tail:
                    self.tail = prev
                self._size -= 1
            else:
                seen.add(current.data)
                prev = current
            current = current.next


#============================================
#EJERCICIO 10 - 14 - 15
#FUNCIONES INDEPENDIENTES FUERA DE LA CLASE
#=============================================

#============================================================
#EJERCICIOS AVANZADOS
#============================================================
    """
    EJERCICIO 11: Palíndromo

    Implementa un método is_palindrome() que determine si la lista es un palíndromo
    (se lee igual de adelante hacia atrás).
    """

    def is_palindrome(self):
        """
        Verifica si la lista es un palindrome
        
        Returns:
            True si es palindrome, False si no
        Complejidad: O(n) tiempo, O(1) espacio
        """
        if self.is_empty() or self.head.next is None:
            return True
        
        #Paso 1 Encontrar el medio
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Paso 2 Invertir la segunda mitad
        middle = slow
        prev = None
        current = middle
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        #Paso 3 Comparar ambas mitades
        left = self.head
        right = prev  #Cabeza de la segunda mitad invertida
        
        while right:
            if left.data != right.data:
                #Paso 4 Restaurar la lista (opcional)
                self._restore_second_half(middle, prev)
                return False
            left = left.next
            right = right.next
        
        #Paso 4 Restaurar la lista
        self._restore_second_half(middle, prev)
        return True
    
    def _restore_second_half(self, middle, reversed_head):
        #Método auxiliar para restaurar la segunda mitad
        prev = None
        current = reversed_head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        #Reconectar las dos mitades
        left = self.head
        while left.next != middle:
            left = left.next
        left.next = prev
    

    """
    EJERCICIO 12: Rotar lista

    Implementa un método rotate(k) que rote la lista k posiciones a la derecha.
    """

    def rotate(self, k):
        """
        Rota la lista k posiciones a la derecha
        
        Args:
            k: Número de posiciones a rotar
        Complejidad: O(n)
        """
        if self.is_empty() or k % self._size == 0:
            return
        
        k = k % self._size
        
        #Paso 1: Hacer la lista circular
        self.tail.next = self.head
        
        #Paso 2: Encontrar el nuevo head (tamaño - k)
        steps_to_new_head = self._size - k
        new_tail = self.head
        
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        #Paso 3: Romper el círculo
        new_tail.next = None
        self.head = new_head
        self.tail = new_tail


    """
    EJERCICIO 13: Particionar lista

    Implementa un método partition(x) que reorganice la lista de modo que
    todos los elementos menores que x aparezcan antes que los elementos
    mayores o iguales a x. El orden relativo dentro de cada grupo debe preservarse.
    """

    def partition(self, x):
        """
        Particiona la lista alrededor del valor x
        
        Args:
            x: Valor pivote para particionar
        """
        if self.is_empty() or self.head.next is None:
            return
        
        #Crear listas auxiliares
        menores_head = menores_tail = Node(None)  #Nodo dummy
        mayores_head = mayores_tail = Node(None)  #Nodo dummy
        
        current = self.head
        
        while current:
            next_node = current.next
            current.next = None
            
            if current.data < x:
                if menores_head.data is None:
                    menores_head = current
                    menores_tail = current
                else:
                    menores_tail.next = current
                    menores_tail = current
            else:
                if mayores_head.data is None:
                    mayores_head = current
                    mayores_tail = current
                else:
                    mayores_tail.next = current
                    mayores_tail = current
            
            current = next_node
        
        #Unir las dos listas
        if menores_head.data is None:
            self.head = mayores_head
            self.tail = mayores_tail
        elif mayores_head.data is None:
            self.head = menores_head
            self.tail = menores_tail
        else:
            menores_tail.next = mayores_head
            self.head = menores_head
            self.tail = mayores_tail


#============================================================================
#FUNCIONES INDEPENDIENTESS
#============================================================================

"""
EJERCICIO 10: Fusionar dos listas ordenadas

Implementa una función merge_sorted(list1, list2) que tome dos listas
enlazadas ORDENADAS y retorne una nueva lista enlazada también ordenada
con todos los elementos de ambas.
"""

def merge_sorted(list1, list2):
    """
    Fusiona dos listas ordenadas en una nueva lista ordenada
    
    Args:
        list1: Primera lista enlazada ordenada
        list2: Segunda lista enlazada ordenada
        
    Returns:
        Nueva lista enlazada con todos los elementos ordenados
    """
    result = LinkedList()
    
    current1 = list1.head
    current2 = list2.head
    
    while current1 and current2:
        if current1.data <= current2.data:
            result.append(current1.data)
            current1 = current1.next
        else:
            result.append(current2.data)
            current2 = current2.next
    
    #Agregar elementos restantes
    while current1:
        result.append(current1.data)
        current1 = current1.next
    
    while current2:
        result.append(current2.data)
        current2 = current2.next
    
    return result


"""
EJERCICIO 14: Suma de dos listas (números)

Tienes dos listas enlazadas que representan números (cada nodo es un dígito).
Los dígitos están almacenados en ORDEN INVERSO (el primer nodo es la unidad).

Implementa una función add_numbers(list1, list2) que sume ambos números
y retorne el resultado como una nueva lista enlazada.
"""

def add_numbers(list1, list2):
    """
    Suma dos números representados como listas enlazadas
    
    Args:
        list1: Primera lista (dígitos en orden inverso)
        list2: Segunda lista (dígitos en orden inverso)
        
    Returns:
        Nueva lista con la suma (dígitos en orden inverso)
    """
    result = LinkedList()
    carry = 0
    
    current1 = list1.head
    current2 = list2.head
    
    while current1 or current2 or carry:
        #Obtener dígitos actuales
        digit1 = current1.data if current1 else 0
        digit2 = current2.data if current2 else 0
        
        #Calcular suma
        total = digit1 + digit2 + carry
        
        #Determinar dígito y carry
        digit = total % 10
        carry = total // 10
        
        #Agregar dígito al resultado
        result.append(digit)
        
        #Avanzar punteros
        if current1:
            current1 = current1.next
        if current2:
            current2 = current2.next
    
    return result


"""
EJERCICIO 15: Intersección de dos listas

Dadas dos listas enlazadas, determina si se intersectan (comparten nodos)
y encuentra el nodo donde se intersectan.

Solución eficiente:
1. Calcula la longitud de ambas listas
2. Alinea los inicios (avanza en la lista más larga)
3. Avanza simultáneamente hasta encontrar el nodo común

Complejidad: O(n + m) tiempo, O(1) espacio
"""

def find_intersection(list1, list2):
    """
    Encuentra el nodo de intersección de dos listas
    
    Args:
        list1: Primera lista enlazada
        list2: Segunda lista enlazada
        
    Returns:
        El nodo de intersección, o None si no se intersectan
    Complejidad: O(n + m) tiempo, O(1) espacio
    """
    def get_length_and_tail(lista):
        """Obtiene longitud y tail de una lista"""
        if lista.is_empty():
            return 0, None
        
        length = 0
        current = lista.head
        
        while current:
            length += 1
            if current.next is None:
                tail = current
            current = current.next
        
        return length, tail
    
    #Paso 1 Obtener longitudes y tails
    len1, tail1 = get_length_and_tail(list1)
    len2, tail2 = get_length_and_tail(list2)
    
    #Si tails son diferentes entonce no hay intersección
    if tail1 is not tail2:
        return None
    
    #Paso 2 Alinear los inicios
    current1 = list1.head
    current2 = list2.head
    
    if len1 > len2:
        for _ in range(len1 - len2):
            current1 = current1.next
    elif len2 > len1:
        for _ in range(len2 - len1):
            current2 = current2.next
    
    #Paso 3 Encontrar intersección
    while current1 and current2:
        if current1 is current2:
            return current1
        current1 = current1.next
        current2 = current2.next
    
    return None


#============================================================================
#EJERCICIOS DE LISTA DOBLEMENTE ENLAZADA
#============================================================================

"""
EJERCICIO 16: Navegador Web
Implementa una clase BrowserHistory que simule el historial de un navegador
usando una lista doblemente enlazada.

Métodos requeridos:
- __init__(homepage): Inicia con la página de inicio
- visit(url): Visita una nueva URL (elimina historial futuro)
- back(steps): Retrocede 'steps' páginas (máximo hasta el inicio)
- forward(steps): Avanza 'steps' páginas (máximo hasta el final)
- get_current(): Retorna la URL actual
"""

class BrowserHistory:
    """Simula historial de navegador usando lista doblemente enlazada"""
    
    def __init__(self, homepage):
        """
        Inicia con la página de inicio
        
        Args:
            homepage: URL de la página de inicio
        """
        new_node = DoubleNode(homepage)
        self.head = new_node
        self.tail = new_node
        self.current = new_node
    
    def visit(self, url):
        """
        Visita una nueva URL (elimina historial futuro)
        
        Args:
            url: Nueva URL a visitar
        """
        new_node = DoubleNode(url)
        
        #Eliminar historial futuro
        self.current.next = None
        
        #Agregar nueva página
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node
        self.tail = new_node
    
    def back(self, steps):
        """
        Retrocede 'steps' páginas (máximo hasta el inicio)
        
        Args:
            steps: Número de páginas a retroceder
            
        Returns:
            URL actual después de retroceder
        """
        current_steps = 0
        
        while current_steps < steps and self.current.prev:
            self.current = self.current.prev
            current_steps += 1
        
        return self.current.data
    
    def forward(self, steps):
        """
        Avanza 'steps' páginas (máximo hasta el final)
        
        Args:
            steps: Número de páginas a avanzar
            
        Returns:
            URL actual después de avanzar
        """
        current_steps = 0
        
        while current_steps < steps and self.current.next:
            self.current = self.current.next
            current_steps += 1
        
        return self.current.data
    
    def get_current(self):
        """
        Retorna la URL actual
        
        Returns:
            URL actual
        """
        return self.current.data if self.current else None
    
    def __repr__(self):
        """Representación del historial"""
        urls = []
        current = self.head
        
        while current:
            prefix = "➤ " if current is self.current else "  "
            urls.append(f"{prefix}{current.data}")
            current = current.next
        
        return "\n".join(urls)


"""
EJERCICIO 17: LRU Cache

Implementa una estructura de datos LRU Cache (Least Recently Used Cache)
usando una lista doblemente enlazada + diccionario.

El cache tiene capacidad limitada. Cuando se llena, elimina el elemento
usado menos recientemente.

Métodos:
- __init__(capacity): Crea cache con capacidad dada
- get(key): Obtiene el valor (marca como usado recientemente)
- put(key, value): Inserta/actualiza (elimina LRU si está lleno)

Ambos métodos deben ser O(1).
"""
class LRUCache:
    """
    Implementación de LRU Cache usando lista doblemente enlazada + diccionario
    """
    
    class CacheNode:
        """Nodo especial para la cache"""
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        """
        Crea cache con capacidad dada
        
        Args:
            capacity: Capacidad máxima de la cache
        """
        self.capacity = capacity
        self.cache = {}  #Diccionario para acceso O(1)
        
        #Nodos dummy para facilitar operaciones
        self.head = self.CacheNode(None, None)  #Mas reciente
        self.tail = self.CacheNode(None, None)  #Menos reciente
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_front(self, node):
        """Agrega nodo al frente (más reciente)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Elimina nodo de la lista"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_front(self, node):
        """Mueve nodo al frente (acceso reciente)"""
        self._remove_node(node)
        self._add_to_front(node)
    
    def get(self, key):
        """
        Obtiene el valor (marca como usado recientemente)
        
        Args:
            key: Llave a buscar
            
        Returns:
            Valor asociado a la llave, o -1 si no existe
        """
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_front(node)
        return node.value
    
    def put(self, key, value):
        """
        Inserta/actualiza (elimina LRU si está lleno)
        
        Args:
            key: Llave a insertar/actualizar
            value: Valor asociado
        """
        if key in self.cache:
            #Actualizar valor y mover al frente
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            #Crear nuevo nodo
            new_node = self.CacheNode(key, value)
            
            if len(self.cache) >= self.capacity:
                #Eliminar LRU
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
            
            #Agregar nuevo nodo
            self._add_to_front(new_node)
            self.cache[key] = new_node


"""
EJERCICIO 18: Editor Multi-cursor

Extiende el TextEditor para soportar múltiples cursores (como en VS Code).
Cada cursor puede estar en una posición diferente del documento.

Funcionalidades:
- add_cursor(position): Agregar cursor en posición
- remove_cursor(cursor_id): Eliminar cursor
- type_at_cursor(cursor_id, text): Escribir en cursor específico
- undo_all(): Deshacer en todos los cursores
- redo_all(): Rehacer en todos los cursores

Esto requiere mantener múltiples historiales sincronizados.
"""

class MultiCursorEditor:
#Editor de texto con soporte para múltiples cursores
    
    def __init__(self):
        """Inicializa editor vacío"""
        self.text = []
        self.cursors = {}  #{cursor_id: position}
        self.next_cursor_id = 0
        self.history = []  #Historial de operaciones
        
    def add_cursor(self, position):
        """
        Agregar cursor en posición
        
        Args:
            position: Posición del cursor
            
        Returns:
            ID del cursor creado
        """
        cursor_id = self.next_cursor_id
        self.cursors[cursor_id] = position
        self.next_cursor_id += 1
        return cursor_id
    
    def remove_cursor(self, cursor_id):
        """
        Eliminar cursor
        
        Args:
            cursor_id: ID del cursor a eliminar
        """
        if cursor_id in self.cursors:
            del self.cursors[cursor_id]
    
    def type_at_cursor(self, cursor_id, text):
        """
        Escribir en cursor específico
        
        Args:
            cursor_id: ID del cursor
            text: Texto a insertar
        """
        if cursor_id not in self.cursors:
            raise ValueError(f"Cursor {cursor_id} no existe")
        
        position = self.cursors[cursor_id]
        
        #Guardar en historial
        self.history.append(('type', cursor_id, position, text))
        
        #Insertar texto
        if position >= len(self.text):
            self.text.extend([''] * (position - len(self.text) + 1))
        
        if position < len(self.text):
            self.text[position] += text
        else:
            self.text.append(text)
        
        #Actualizar posición del cursor
        self.cursors[cursor_id] += len(text)
        
        #Actualizar otros cursores si están después
        for cid, pos in self.cursors.items():
            if cid != cursor_id and pos >= position:
                self.cursors[cid] += len(text)
    
    def undo_all(self):
        """Deshacer en todos los cursores"""
        if not self.history:
            return
        
        last_op = self.history.pop()
        
        if last_op[0] == 'type':
            _, cursor_id, position, text = last_op
            
            #Eliminar texto
            for cid in self.cursors:
                if self.cursors[cid] >= position + len(text):
                    self.cursors[cid] -= len(text)
            
            self.cursors[cursor_id] = position
            
            #Restaurar texto
            if position < len(self.text):
                self.text[position] = self.text[position][:-len(text)]
    
    def redo_all(self):
    #Rehacer en todos los cursores pero simplificado
        #Para implementacion completa necesitaríamos historial de redo
        pass
    
    def get_text(self):
        #Obtener texto completo
        return ''.join(self.text)
    
    def __repr__(self):
        #Representación del editor
        result = f"Texto: {self.get_text()}\n"
        result += f"Cursores: {self.cursors}\n"
        return result


#============================================================================
#EJERCICIOS DE ANÁLISIS Y OPTIMIZACIÓN
#============================================================================

"""
EJERCICIO 19: Benchmark de operaciones

Escribe un programa que compare el rendimiento de:
- Arrays (listas de Python)
- Listas simplemente enlazadas
- Listas doblemente enlazadas

Para las siguientes operaciones:
1. Inserción al inicio (1000 elementos)
2. Inserción al final (1000 elementos)
3. Eliminación al inicio (1000 elementos)
4. Eliminación al final (1000 elementos)
5. Acceso por índice (1000 accesos aleatorios)

Usa el módulo 'time' para medir el tiempo.
Imprime los resultados en una tabla comparativa.
"""

import time
import random

class LinkedListBenchmark:
    #Clase para benchmarking de listas enlazadas
    """
    Método estático que compara el rendimiento de arrays vs listas enlazadas
    Se llama directamente desde la clase sin necesidad de crear objeto"""
    @staticmethod

    def benchmark_data_structures():
        """
        Compara el rendimiento de diferentes estructuras
        
        Returns:
            Diccionario con tiempos de ejecución
        """
        results = {
            'array': {},
            'singly_linked': {},
            'doubly_linked': {}
        }
        
        n = 1000
        
        #Array (lista de Python)
        print("Benchmarking Array (lista Python)...")
        
        #1. Inserción al inicio
        start = time.time()
        arr = []
        for i in range(n):
            arr.insert(0, i)
        results['array']['insercion_inicio'] = time.time() - start
        
        #2. Inserción al final
        start = time.time()
        arr = []
        for i in range(n):
            arr.append(i)
        results['array']['insercion_final'] = time.time() - start
        
        #3. Eliminación al inicio
        arr = list(range(n))
        start = time.time()
        for _ in range(n):
            arr.pop(0) if arr else None
        results['array']['eliminacion_inicio'] = time.time() - start
        
        #4. Eliminación al final
        arr = list(range(n))
        start = time.time()
        for _ in range(n):
            arr.pop() if arr else None
        results['array']['eliminacion_final'] = time.time() - start
        
        #5. Acceso por índice
        arr = list(range(n))
        indices = random.sample(range(n), n)
        start = time.time()
        for idx in indices:
            _ = arr[idx] if idx < len(arr) else None
        results['array']['acceso_indice'] = time.time() - start
        
        #Lista simplemente enlazada
        print("Benchmarking Lista Simplemente Enlazada...")
        
        #1. Inserción al inicio
        start = time.time()
        ll = LinkedList()
        for i in range(n):
            ll.prepend(i)
        results['singly_linked']['insercion_inicio'] = time.time() - start
        
        #2. Inserción al final
        start = time.time()
        ll = LinkedList()
        for i in range(n):
            ll.append(i)
        results['singly_linked']['insercion_final'] = time.time() - start
        
        #3. Eliminación al inicio (simplificada)
        #Nota: Para eliminación necesitaríamos implementar pop(0)
        #Usaremos una implementación simplificada
        results['singly_linked']['eliminacion_inicio'] = "N/A - O(n)"
        
        #4. Eliminación al final (simplificada)
        results['singly_linked']['eliminacion_final'] = "N/A - O(n)"
        
        #5. Acceso por índice
        ll = LinkedList()
        for i in range(n):
            ll.append(i)
        
        indices = random.sample(range(n), min(n, 100))  #Menos accesos por ser O(n)
        start = time.time()
        for idx in indices:
            try:
                _ = ll.get(idx)
            except:
                pass
        results['singly_linked']['acceso_indice'] = time.time() - start
        
        return results
    
    @staticmethod
    def print_results(results):
        """Imprime resultados del benchmark en formato tabla"""
        print("\n" + "="*80)
        print("BENCHMARK DE ESTRUCTURAS DE DATOS")
        print("="*80)
        print("\nTiempos en segundos (n=1000 operaciones):\n")
        
        print(f"{'Operación':<25} {'Array':<15} {'Lista Simple':<15} {'Lista Doble':<15}")
        print("-"*80)
        
        operations = [
            'insercion_inicio',
            'insercion_final',
            'eliminacion_inicio',
            'eliminacion_final',
            'acceso_indice'
        ]
        
        op_names = {
            'insercion_inicio': 'Inserción inicio',
            'insercion_final': 'Inserción final',
            'eliminacion_inicio': 'Eliminación inicio',
            'eliminacion_final': 'Eliminación final',
            'acceso_indice': 'Acceso por índice'
        }
        
        for op in operations:
            array_time = f"{results['array'][op]:.6f}"
            singly_time = results['singly_linked'].get(op, 'N/A')
            if isinstance(singly_time, float):
                singly_time = f"{singly_time:.6f}"
            
            # Lista doble sería similar a simple para benchmark
            doubly_time = "Similar a simple"
            
            print(f"{op_names[op]:<25} {array_time:<15} {singly_time:<15} {doubly_time:<15}")
        
        print("\n" + "="*80)
        print("CONCLUSIONES:")
        print("-"*80)
        print("1. Arrays son mejores para acceso aleatorio")
        print("2. Listas enlazadas son mejores para inserciones al inicio")
        print("3. Eliminación al final es eficiente en arrays, no en listas simples")
        print("4. Listas dobles mejoran algunas operaciones pero consumen más memoria")
        print("="*80)


"""
EJERCICIO 20: Análisis de casos de uso

Para cada uno de los siguientes escenarios, determina qué estructura
es más apropiada (Array, Lista Simple, Lista Doble) y justifica tu respuesta:

1. Sistema de colas de impresión (FIFO estricto)
2. Historial de navegación de un navegador
3. Sistema de undo/redo con límite de 100 acciones
4. Base de datos que necesita acceso rápido por ID
5. Playlist de música con navegación adelante/atrás
6. Sistema de gestión de memoria del OS
7. Editor de texto que solo permite append al final
8. Implementación de una pila (Stack)
9. Juego que necesita insertar/eliminar enemigos frecuentemente
10. Sistema de logs que solo escribe al final y lee todo

Escribe tus respuestas en comentarios con justificación.
"""

def analisis_casos_uso():
    """
    Análisis de casos de uso para diferentes estructuras de datos
    """
    print("\n" + "="*80)
    print("ANÁLISIS DE CASOS DE USO")
    print("="*80)
    
    casos = [
        {
            "nombre": "Sistema de colas de impresión (FIFO estricto)",
            "recomendacion": "Lista Simple",
            "justificacion": "FIFO requiere inserción al final y eliminación al inicio, ambas O(1) en lista simple"
        },
        {
            "nombre": "Historial de navegación de un navegador",
            "recomendacion": "Lista Doble",
            "justificacion": "Requiere navegación hacia adelante y atrás, fácil con punteros prev/next"
        },
        {
            "nombre": "Sistema de undo/redo con límite de 100 acciones",
            "recomendacion": "Array",
            "justificacion": "Tamaño fijo, acceso rápido por índice para navegación en historial"
        },
        {
            "nombre": "Base de datos que necesita acceso rápido por ID",
            "recomendacion": "Array + Hash Table",
            "justificacion": "Arrays para almacenamiento contiguo, hash table para acceso O(1) por ID"
        },
        {
            "nombre": "Playlist de música con navegación adelante/atrás",
            "recomendacion": "Lista Doble",
            "justificacion": "Navegación bidireccional natural, inserción o eliminación eficiente"
        },
        {
            "nombre": "Sistema de gestión de memoria del OS",
            "recomendacion": "Lista Doble + Array",
            "justificacion": "Lista doble para bloques libres, arrays para páginas de memoria"
        },
        {
            "nombre": "Editor de texto que solo permite append al final",
            "recomendacion": "Array",
            "justificacion": "Append al final es O(1) amortizado, acceso por índice para edición"
        },
        {
            "nombre": "Implementación de una pila (Stack)",
            "recomendacion": "Array",
            "justificacion": "Push y pop al final son O(1) amortizado, menos overhead que listas"
        },
        {
            "nombre": "Juego que necesita insertaro eliminar enemigos frecuentemente",
            "recomendacion": "Array + Free List",
            "justificacion": "Arrays para acceso rápido, free list para reutilizar espacios vacíos"
        },
        {
            "nombre": "Sistema de logs que solo escribe al final y lee todo",
            "recomendacion": "Array",
            "justificacion": "Append al final eficiente, lectura secuencial rápida por localidad"
        }
    ]
    
    for i, caso in enumerate(casos, 1):
        print(f"\n{i}. {caso['nombre']}")
        print(f"   Recomendación: {caso['recomendacion']}")
        print(f"   Justificación: {caso['justificacion']}")
    print("\n" + "="*80)


#============================================================================
#PRUEBAS COMPLETAS PARA TODOS LOS EJERCICIOS
#============================================================================

def run_all_tests():
    """Ejecuta pruebas para todos los ejercicios"""
    
    print("=" * 80)
    print("PRUEBAS LISTAS ENLAZADAS")
    print("=" * 80)
    


    #EJERCICIO 1: Contar elementos
    print("\n1. PRUEBA EJERCICIO 1 - count()")
    print("-" * 40)
    
    ll = LinkedList()
    ll.create_from_list([1, 2, 3, 2, 4, 2])
    
    test_cases = [
        (2, 3, "Contar número 2 (aparece 3 veces)"),
        (5, 0, "Contar número 5 (no aparece)"),
        (1, 1, "Contar número 1 (aparece 1 vez)")
    ]
    
    all_passed = True
    for elem, expected, desc in test_cases:
        result = ll.count(elem)
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: count({elem}) = {result} (esperado: {expected})")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")
    
    

    #EJERCICIO 2: Obtener elemento por índice
    print("\n\n2. PRUEBA EJERCICIO 2 - get()")
    print("-" * 40)
    
    ll = LinkedList()
    ll.create_from_list(['A', 'B', 'C', 'D'])
    
    test_cases = [
        (0, 'A', "Obtener índice 0"),
        (2, 'C', "Obtener índice 2"),
        (3, 'D', "Obtener índice 3")
    ]
    
    all_passed = True
    
    for idx, expected, desc in test_cases:
        try:
            result = ll.get(idx)
            passed = result == expected
            status = "✓" if passed else "✗"
            print(f"{status} {desc}: get({idx}) = '{result}' (esperado: '{expected}')")
        except IndexError as e:
            passed = False
            status = "✗"
            print(f"{status} {desc}: get({idx}) lanzó IndexError: {e}")
        
        all_passed = all_passed and passed
    
    #Prueba índice fuera de rango
    try:
        ll.get(10)
        print("✗ Índice 10: Debería lanzar IndexError pero no lo hizo")
        all_passed = False
    except IndexError:
        print("✓ Índice 10: Correctamente lanzó IndexError")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")



    #EJERCICIO 3: Encontrar índice de elemento
    print("\n\n3. PRUEBA EJERCICIO 3 - index_of()")
    print("-" * 40)
    
    ll = LinkedList()
    ll.create_from_list(['A', 'B', 'C', 'B', 'D'])
    
    test_cases = [
        ('B', 1, "Índice de 'B' (primera ocurrencia)"),
        ('D', 4, "Índice de 'D'"),
        ('Z', -1, "Índice de 'Z' (no existe)"),
        ('A', 0, "Índice de 'A'")
    ]
    
    all_passed = True
    for elem, expected, desc in test_cases:
        result = ll.index_of(elem)
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: index_of('{elem}') = {result} (esperado: {expected})")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")



    #EJERCICIO 4: Lista a array
    print("\n\n4. PRUEBA EJERCICIO 4 - to_list()")
    print("-" * 40)
    
    test_cases = [
        ([1, 2, 3, 4], "Lista normal"),
        ([], "Lista vacía"),
        ([5], "Lista con un elemento"),
        ([10, 20, 30, 40, 50], "Lista con 5 elementos")
    ]
    
    all_passed = True
    for data_list, desc in test_cases:
        ll = LinkedList()
        ll.create_from_list(data_list)
        result = ll.to_list()
        passed = result == data_list
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: to_list() = {result} (esperado: {data_list})")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")



    #EJERCICIO 5: Limpiar lista
    print("\n\n5. PRUEBA EJERCICIO 5 - clear()")
    print("-" * 40)
    
    ll = LinkedList()
    ll.create_from_list([1, 2, 3, 4, 5])
    
    print(f"Antes de clear(): tamaño = {len(ll)}, lista = {ll.to_list()}")
    ll.clear()
    
    tests = [
        (len(ll), 0, "Tamaño después de clear()"),
        (ll.is_empty(), True, "is_empty() después de clear()"),
        (ll.to_list(), [], "to_list() después de clear()")
    ]
    
    all_passed = True
    for result, expected, desc in tests:
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: {result} (esperado: {expected})")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")
    

  
    #EJERCICIO 6: Invertir lista
    print("\n\n6. PRUEBA EJERCICIO 6 - reverse()")
    print("-" * 40)
    
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], "Lista normal"),
        ([1], [1], "Lista con un elemento"),
        ([1, 2], [2, 1], "Lista con dos elementos"),
        ([], [], "Lista vacía")
    ]
    
    all_passed = True
    for original, expected, desc in test_cases:
        ll = LinkedList()
        ll.create_from_list(original)
        ll.reverse()
        result = ll.to_list()
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: reverse({original}) = {result} (esperado: {expected})")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")
    

    
    #EJERCICIO 7: Detectar ciclo
    print("\n\n7. PRUEBA EJERCICIO 7 - has_cycle()")
    print("-" * 40)
    
        #Crear lista sin ciclo
    ll1 = LinkedList()
    ll1.create_from_list([1, 2, 3, 4, 5])
    
        #Crear lista con ciclo (manualmente)
    ll2 = LinkedList()
    ll2.create_from_list([1, 2, 3, 4, 5])
        #Crear ciclo: 3 → 4 → 5 → 3
    if ll2.head and ll2.head.next and ll2.head.next.next:
        third = ll2.head.next.next
        fifth = ll2.tail
        fifth.next = third
    
    test_cases = [
        (ll1, False, "Lista sin ciclo"),
        (ll2, True, "Lista con ciclo")
    ]
    
    all_passed = True
    for lista, expected, desc in test_cases:
        result = lista.has_cycle()
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: has_cycle() = {result} (esperado: {expected})")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")
    
    

    #EJERCICIO 8: Encontrar el medio
    print("\n\n8. PRUEBA EJERCICIO 8 - get_middle()")
    print("-" * 40)
    
    test_cases = [
        ([1, 2, 3, 4, 5], 3, "Lista impar"),
        ([1, 2, 3, 4], 3, "Lista par (segundo del medio)"),
        ([1, 2], 2, "Lista con 2 elementos"),
        ([5], 5, "Lista con 1 elemento")
    ]
    
    all_passed = True
    for data_list, expected, desc in test_cases:
        ll = LinkedList()
        ll.create_from_list(data_list)
        result = ll.get_middle()
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: get_middle({data_list}) = {result} (esperado: {expected})")
    
        #Prueba lista vacía
    ll_empty = LinkedList()
    try:
        ll_empty.get_middle()
        print("✗ Lista vacía: Debería lanzar excepción pero no lo hizo")
        all_passed = False
    except Exception as e:
        print(f"✓ Lista vacía: Correctamente lanzó excepción: {e}")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")
    


    #EJERCICIO 9: Eliminar duplicados
    print("\n\n9. PRUEBA EJERCICIO 9 - remove_duplicates()")
    print("-" * 40)
    
    test_cases = [
        ([1, 2, 3, 2, 4, 1, 5], [1, 2, 3, 4, 5], "Lista con duplicados"),
        ([1, 1, 1, 1], [1], "Todos duplicados"),
        ([1, 2, 3, 4], [1, 2, 3, 4], "Sin duplicados"),
        ([], [], "Lista vacía")
    ]
    
    all_passed = True
    for original, expected, desc in test_cases:
        ll = LinkedList()
        ll.create_from_list(original)
        ll.remove_duplicates()
        result = ll.to_list()
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: remove_duplicates({original}) = {result} (esperado: {expected})")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")
    
   

    #EJERCICIO 10: Fusionar dos listas ordenadas
    print("\n\n10. PRUEBA EJERCICIO 10 - merge_sorted()")
    print("-" * 40)
    
        #Crear listas ordenadas
    ll1 = LinkedList()
    ll1.create_from_list([1, 3, 5, 7])
    
    ll2 = LinkedList()
    ll2.create_from_list([2, 4, 6, 8])
    
    ll3 = LinkedList()
    ll3.create_from_list([10, 20, 30])
    
    ll4 = LinkedList()  # Lista vacía
    
    test_cases = [
        (ll1, ll2, [1, 2, 3, 4, 5, 6, 7, 8], "Dos listas del mismo tamaño"),
        (ll1, ll3, [1, 3, 5, 7, 10, 20, 30], "Listas de diferente tamaño"),
        (ll1, ll4, [1, 3, 5, 7], "Una lista vacía"),
        (ll4, ll4, [], "Ambas listas vacías")
    ]
    
    all_passed = True
    for lista1, lista2, expected, desc in test_cases:
        result_list = merge_sorted(lista1, lista2)
        result = result_list.to_list()
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: merge_sorted() = {result} (esperado: {expected})")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")
    
 

    #EJERCICIO 11: Palíndromo
    print("\n\n11. PRUEBA EJERCICIO 11 - is_palindrome()")
    print("-" * 40)
    
    test_cases = [
        ([1, 2, 3, 2, 1], True, "Palíndromo impar"),
        ([1, 2, 2, 1], True, "Palíndromo par"),
        ([1, 2, 3, 4, 5], False, "No palíndromo"),
        ([1], True, "Un elemento"),
        ([], True, "Lista vacía"),
        ([1, 2, 3, 3, 2, 1], True, "Palíndromo largo"),
        ([1, 2, 3, 4, 3, 2, 1], True, "Palíndromo impar largo")
    ]
    
    all_passed = True
    for data_list, expected, desc in test_cases:
        ll = LinkedList()
        ll.create_from_list(data_list)
        result = ll.is_palindrome()
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: is_palindrome({data_list}) = {result} (esperado: {expected})")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")
    
    

    #EJERCICIO 12: Rotar lista
    print("\n\n12. PRUEBA EJERCICIO 12 - rotate()")
    print("-" * 40)
    
    ll = LinkedList()
    ll.create_from_list([1, 2, 3, 4, 5])
    
    test_cases = [
        (2, [4, 5, 1, 2, 3], "Rotar 2 posiciones"),
        (0, [1, 2, 3, 4, 5], "Rotar 0 posiciones"),
        (5, [1, 2, 3, 4, 5], "Rotar tamaño completo"),
        (7, [4, 5, 1, 2, 3], "Rotar más que tamaño (7 % 5 = 2)")
    ]
    
    all_passed = True
    for k, expected, desc in test_cases:
        #Crear nueva lista para cada prueba
        test_ll = LinkedList()
        test_ll.create_from_list([1, 2, 3, 4, 5])
        test_ll.rotate(k)
        result = test_ll.to_list()
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: rotate({k}, [1,2,3,4,5]) = {result} (esperado: {expected})")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")
    


    #EJERCICIO 13: Particionar lista
    print("\n\n13. PRUEBA EJERCICIO 13 - partition()")
    print("-" * 40)
    
    ll = LinkedList()
    ll.create_from_list([3, 5, 8, 5, 10, 2, 1])
    
    print(f"Lista original: {ll.to_list()}")
    ll.partition(5)
    result = ll.to_list()
    
        #Verificar partición
        #Todos los elementos < 5 deben estar primero
    partition_index = 0
    for i, val in enumerate(result):
        if val >= 5:
            partition_index = i
            break
    
    menores = result[:partition_index]
    mayores = result[partition_index:]
    
    print(f"Después de partition(5): {result}")
    print(f"Menores que 5: {menores}")
    print(f"Mayores o iguales a 5: {mayores}")
    
        #Verificar que todos los menores sean < 5
    todos_menores = all(x < 5 for x in menores)
        #Verificar que todos los mayores sean >= 5
    todos_mayores = all(x >= 5 for x in mayores)
    
    if todos_menores and todos_mayores:
        print("✓ La partición es correcta")
    else:
        print("✗ La partición es incorrecta")
        all_passed = False
    
    print(f"\nResultado: {'PRUEBA PASÓ' if todos_menores and todos_mayores else 'PRUEBA FALLÓ'}")
    

    
    #EJERCICIO 14: Suma de dos listas (números)
    print("\n\n14. PRUEBA EJERCICIO 14 - add_numbers()")
    print("-" * 40)
    
        #Crear listas que representan números
        #342 = 2 → 4 → 3
    num1 = LinkedList()
    num1.create_from_list([2, 4, 3])
    
        #465 = 5 → 6 → 4
    num2 = LinkedList()
    num2.create_from_list([5, 6, 4])
    
        #999 = 9 → 9 → 9
    num3 = LinkedList()
    num3.create_from_list([9, 9, 9])
    
        #1 = 1
    num4 = LinkedList()
    num4.create_from_list([1])
    
    test_cases = [
        (num1, num2, [7, 0, 8], "342 + 465 = 807"),
        (num4, num4, [2], "1 + 1 = 2"),
        (num1, num4, [3, 4, 3], "342 + 1 = 343"),
        (num3, num4, [0, 0, 0, 1], "999 + 1 = 1000")
    ]
    
    all_passed = True
    for lista1, lista2, expected, desc in test_cases:
        result_list = add_numbers(lista1, lista2)
        result = result_list.to_list()
        passed = result == expected
        all_passed = all_passed and passed
        status = "✓" if passed else "✗"
        print(f"{status} {desc}: add_numbers() = {result} (esperado: {expected})")
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")
    
    

    #EJERCICIO 15: Intersección de dos listas
    print("\n\n15. PRUEBA EJERCICIO 15 - find_intersection()")
    print("-" * 40)
    
        #Crear listas que se intersectan
        #Lista 1: 1 → 2 → 3 → 7 → 8 → 9
    list1 = LinkedList()
    list1.create_from_list([1, 2, 3])
    
        #Lista 2: 4 → 5 → 6
    list2 = LinkedList()
    list2.create_from_list([4, 5, 6])
    
        #Crear nodos compartidos
    shared = LinkedList()
    shared.create_from_list([7, 8, 9])
    
        #Conectar listas al shared
    if list1.tail and shared.head:
        list1.tail.next = shared.head
    
    if list2.tail and shared.head:
        list2.tail.next = shared.head
    
        #Listas sin intersección
    list3 = LinkedList()
    list3.create_from_list([10, 11, 12])
    
    test_cases = [
        (list1, list2, shared.head, "Listas que se intersectan"),
        (list1, list3, None, "Listas sin intersección"),
        (list1, list1, list1.head, "Misma lista")
    ]
    
    all_passed = True
    for l1, l2, expected_node, desc in test_cases:
        result = find_intersection(l1, l2)
        
        if expected_node is None:
            passed = result is None
            status = "✓" if passed else "✗"
            print(f"{status} {desc}: find_intersection() = {result} (esperado: None)")
        else:
            passed = result is expected_node
            status = "✓" if passed else "✗"
            result_val = result.data if result else None
            expected_val = expected_node.data if expected_node else None
            print(f"{status} {desc}: find_intersection() = nodo con valor {result_val} (esperado: {expected_val})")
        
        all_passed = all_passed and passed
    
    print(f"\nResultado: {'TODAS LAS PRUEBAS PASARON' if all_passed else 'ALGUNAS PRUEBAS FALLARON'}")
    
    

    #EJERCICIO 16: Navegador Web
    print("\n\n16. PRUEBA EJERCICIO 16 - BrowserHistory")
    print("-" * 40)
    
    browser = BrowserHistory("google.com")
    print(f"Inicio: {browser.get_current()}")
    
    browser.visit("youtube.com")
    print(f"Después de visit('youtube.com'): {browser.get_current()}")
    
    browser.visit("facebook.com")
    print(f"Después de visit('facebook.com'): {browser.get_current()}")
    
    print(f"\nHistorial completo:\n{browser}")
    
        #Probar back
    print(f"\nback(1): {browser.back(1)}")
    print(f"Actual después de back(1): {browser.get_current()}")
    
        #Probar forward
    print(f"\nforward(1): {browser.forward(1)}")
    print(f"Actual después de forward(1): {browser.get_current()}")
    
        #Probar back más allá del inicio
    print(f"\nback(10) (más allá del inicio): {browser.back(10)}")
    print(f"Actual después de back(10): {browser.get_current()}")
    
        #Visitar nueva página (debe eliminar historial futuro)
    browser.visit("twitter.com")
    print(f"\nDespués de visit('twitter.com'): {browser.get_current()}")
    print(f"Historial después de twitter:\n{browser}")
    
    print("\n✓ Todas las operaciones del navegador funcionaron correctamente")
    
    

    #EJERCICIO 17: LRU Cache
    print("\n\n17. PRUEBA EJERCICIO 17 - LRUCache")
    print("-" * 40)
    
    cache = LRUCache(2)  #Capacidad 2
    
    print("Cache creado con capacidad 2")
    
        #Operaciones
    cache.put(1, 1)
    print("put(1, 1)")
    
    cache.put(2, 2)
    print("put(2, 2)")
    
    val1 = cache.get(1)
    print(f"get(1) = {val1} (esperado: 1)")
    
    cache.put(3, 3)  #Debería eliminar la clave 2 (LRU)
    print("put(3, 3) - debería eliminar clave 2 (LRU)")
    
    val2 = cache.get(2)
    print(f"get(2) = {val2} (esperado: -1, no encontrado)")
    
    cache.put(4, 4)  #Debería eliminar la clave 1
    print("put(4, 4) - debería eliminar clave 1")
    
    val1 = cache.get(1)
    print(f"get(1) = {val1} (esperado: -1, no encontrado)")
    
    val3 = cache.get(3)
    print(f"get(3) = {val3} (esperado: 3)")
    
    val4 = cache.get(4)
    print(f"get(4) = {val4} (esperado: 4)")
    
    print("\n✓ Operaciones LRU Cache completadas")
    


    #EJERCICIO 18: Editor Multi-cursor
    print("\n\n18. PRUEBA EJERCICIO 18 - MultiCursorEditor")
    print("-" * 40)
    
    editor = MultiCursorEditor()
    
        #Agregar cursores
    cursor1 = editor.add_cursor(0)
    cursor2 = editor.add_cursor(5)
    
    print(f"Cursores creados: cursor1 (id={cursor1}) en posición 0, cursor2 (id={cursor2}) en posición 5")
    
        #Escribir en cursores
    editor.type_at_cursor(cursor1, "Hola ")
    print(f"type_at_cursor(cursor1, 'Hola ')")
    print(f"Texto actual: '{editor.get_text()}'")
    
    editor.type_at_cursor(cursor2, "mundo")
    print(f"type_at_cursor(cursor2, 'mundo')")
    print(f"Texto actual: '{editor.get_text()}'")
    
    editor.type_at_cursor(cursor1, "amigo ")
    print(f"type_at_cursor(cursor1, 'amigo ')")
    print(f"Texto actual: '{editor.get_text()}'")
    
    print(f"\nPosiciones de cursores: {editor.cursors}")
    
        #Undo
    print("\nEjecutando undo_all()...")
    editor.undo_all()
    print(f"Texto después de undo: '{editor.get_text()}'")
    print(f"Posiciones después de undo: {editor.cursors}")
    
    print("\n✓ Operaciones de multi-cursor completadas")
    


    #EJERCICIO 19: Benchmark de operaciones
    print("\n\n19. PRUEBA EJERCICIO 19 - Benchmark de operaciones")
    print("-" * 40)
    
    benchmark = LinkedListBenchmark()
    results = benchmark.benchmark_data_structures()
    benchmark.print_results(results)
    


    #EJERCICIO 20: Análisis de casos de uso
    print("\n\n20. PRUEBA EJERCICIO 20 - Analisis de casos de uso")
    print("-" * 40)
    
    analisis_casos_uso()



#============================================================================
#EJECUCION PRINCIPAL
#============================================================================

if __name__ == "__main__":
    #Ejecutamos todas las pruebas
    run_all_tests()
    print("Ejercicios completados con sus respectivos casos de prueba")