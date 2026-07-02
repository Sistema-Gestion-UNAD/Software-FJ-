"""
---------------------------------------------------------
Archivo: servicio.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
    Clase abstracta que representa un servicio
    ofrecido por la empresa Software FJ.
---------------------------------------------------------
"""

from abc import ABC, abstractmethod

from entidades.entidad import Entidad
from excepciones.excepciones import (
    ParametroInvalidoError,
    ServicioNoDisponibleError
)


class Servicio(Entidad, ABC):
    """
    Clase abstracta que representa un servicio.
    """

    def __init__(
        self,
        nombre: str,
        costo_base: float,
        disponible: bool = True
    ):
        super().__init__()

        self.nombre = nombre
        self.costo_base = costo_base
        self.disponible = disponible

    # ==================================================
    # Nombre
    # ==================================================

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):

        if not isinstance(valor, str):
            raise ParametroInvalidoError(
                "El nombre del servicio debe ser texto."
            )

        valor = valor.strip()

        if len(valor) < 3:
            raise ParametroInvalidoError(
                "El nombre del servicio debe tener al menos 3 caracteres."
            )

        self._nombre = valor.title()

    # ==================================================
    # Costo Base
    # ==================================================

    @property
    def costo_base(self) -> float:
        return self._costo_base

    @costo_base.setter
    def costo_base(self, valor: float):

        try:
            valor = float(valor)

        except ValueError as error:

            raise ParametroInvalidoError(
                "El costo base debe ser numérico."
            ) from error

        if valor <= 0:

            raise ParametroInvalidoError(
                "El costo base debe ser mayor que cero."
            )

        self._costo_base = valor

    # ==================================================
    # Disponible
    # ==================================================

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool):

        self._disponible = bool(valor)

    # ==================================================
    # Validación
    # ==================================================

    def validar_disponibilidad(self):
        """
        Verifica si el servicio se encuentra disponible.
        """

        if not self.disponible:

            raise ServicioNoDisponibleError(
                f"El servicio '{self.nombre}' no se encuentra disponible."
            )

    # ==================================================
    # Métodos Abstractos
    # ==================================================

    @abstractmethod
    def calcular_costo(
        self,
        horas: int,
        descuento: float = 0.0,
        impuesto: float = 0.0
    ) -> float:
        """
        Calcula el costo del servicio.

        Args:
            horas: Duración del servicio.
            descuento: Descuento opcional.
            impuesto: Impuesto opcional.
        """
        pass

    @abstractmethod
    def descripcion(self) -> str:
        """
        Devuelve una descripción del servicio.
        """
        pass

    @abstractmethod
    def mostrar_informacion(self) -> str:
        """
        Devuelve la información completa del servicio.
        """
        pass

    # ==================================================

    def __str__(self) -> str:

        estado = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        return (
            f"{self.nombre} | "
            f"${self.costo_base:,.2f} | "
            f"{estado}"
        )