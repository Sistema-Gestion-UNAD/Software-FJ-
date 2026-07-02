"""
---------------------------------------------------------
Archivo: logger.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
    Gestiona el registro de eventos y errores del
    sistema mediante archivos de log.
---------------------------------------------------------
"""

import logging
import os


class Logger:
    """
    Clase encargada de registrar eventos del sistema.
    """

    _configurado = False

    @classmethod
    def configurar(cls):
        """
        Configura el sistema de logs.
        """

        if cls._configurado:
            return

        os.makedirs("logs", exist_ok=True)

        logging.basicConfig(
            filename="logs/sistema.log",
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            encoding="utf-8"
        )

        cls._configurado = True

    # ==================================================

    @classmethod
    def info(cls, mensaje: str):
        """
        Registra un mensaje informativo.
        """

        cls.configurar()
        logging.info(mensaje)

    # ==================================================

    @classmethod
    def warning(cls, mensaje: str):
        """
        Registra una advertencia.
        """

        cls.configurar()
        logging.warning(mensaje)

    # ==================================================

    @classmethod
    def error(cls, mensaje: str):
        """
        Registra un error.
        """

        cls.configurar()
        logging.error(mensaje)

    # ==================================================

    @classmethod
    def critical(cls, mensaje: str):
        """
        Registra un error crítico.
        """

        cls.configurar()
        logging.critical(mensaje)