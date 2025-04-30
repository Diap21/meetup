# mi_flujo.py
from prefect import flow

@flow
def hello():
    print("¡Funciona?")

if __name__ == "__main__":
    hello()