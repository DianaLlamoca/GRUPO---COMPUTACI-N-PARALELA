# PARTE 1: TEORÍA
## 1) ¿Cuáles son las diferencias entre concurrencia y paralelismo? ¿En qué escenario es preferible usar concurrencia sobre paralelismo y viceversa?

**-La concurrencia implica que se gestionen múltiples tareas a la misma vez, pero que no necesariamente se estén ejecutando al mismo. Mientras que el paralelismo sí implica concurrencia y además, que las tareas se ejecuten simultáneamente.**

**-La concurrencia es preferible usarla en operaciones de I/O, es decir, que las tareas impliquen un tiempo de espera. Mientras que el paralelismo es mejor en operaciones de CPU.**
