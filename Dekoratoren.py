import time

# Timer-Dekorator
def timer_dekorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Ausführungszeit: {end_time - start_time:.4f} Sekunden")
        return result
    return wrapper

# Beispiel-Funktion, die den Timer-Dekorator verwendet
@timer_dekorator
def beispiel_funktion():
    # Simuliert eine Verarbeitungszeit
    time.sleep(2)

# Aufrufen der dekorierten Funktion
beispiel_funktion()