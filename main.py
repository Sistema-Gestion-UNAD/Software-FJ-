"""
---------------------------------------------------------
Archivo: main.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
Punto de entrada principal de la aplicación.
Ejecuta la simulación completa del sistema.
---------------------------------------------------------
"""

from pruebas.simulacion import ejecutar_simulacion
from utilidades.logger import Logger


def main():
    """
    Función principal del sistema.
    """

    try:
        Logger.info("========== INICIO DEL SISTEMA ==========")

        ejecutar_simulacion()

    except Exception as error:
        Logger.critical(
            f"Error crítico durante la ejecución: {error}"
        )
        print("\nSe produjo un error crítico.")
        print(error)

    finally:
        Logger.info("=========== FIN DEL SISTEMA ===========")
        print("\nPrograma finalizado correctamente.")


if __name__ == "__main__":
    main()