# Implementações de Fatorial em python

O objetivo deste repositório é mostrar duas diferentes versões de algoritmos para resolução do fatorial

## Authors

* Iago Felipe

## Fatorial Iterativo
```python
def Fatorial(n):
    for i in range(n-1, 0, -1):
        n = n*i
    return n
```

## Fatorial Recursivo
```python
def Fatorial_rec(n):
    if (n <= 1):
        return 1
    else: 
        return n * Fatorial_rec(n - 1)
```
