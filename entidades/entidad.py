"""
---------------------------------------------------------
Archivo: entidad.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
Clase abstracta base para todas las entidades del sistema.
---------------------------------------------------------
"""

from abc import ABC
from datetime import datetime


class Entidad(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.
    Proporciona un identificador único y la fecha de creación.
    """

    _contador_id = 1

    def __init__(self):
        """
        Inicializa una nueva entidad.
        """

        self._id = Entidad._contador_id
        Entidad._contador_id += 1

        self._fecha_creacion = datetime.now()

    # ==================================================
    # Propiedad ID
    # ==================================================

    @property
    def id(self) -> int:
        """
        Retorna el identificador único de la entidad.
        """
        return self._id

    # ==================================================
    # Propiedad fecha de creación
    # ==================================================

    @property
    def fecha_creacion(self) -> datetime:
        """
        Retorna la fecha y hora de creación del objeto.
        """
        return self._fecha_creacion

    # ==================================================

    def __str__(self) -> str:
        """
        Representación en texto de la entidad.
        """

        return (
            f"ID: {self.id} | "
            f"Fecha de creación: "
            f"{self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
        )