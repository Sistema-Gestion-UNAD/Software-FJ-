"""
---------------------------------------------------------
Archivo: asesoria.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
    Servicio especializado para asesorías.
---------------------------------------------------------
"""

from servicios.servicio import Servicio
from excepciones.excepciones import (
    DuracionInvalidaError,
    ParametroInvalidoError
)


class Asesoria(Servicio):
    """
    Representa un servicio de asesoría especializada.
    """

    def __init__(
        self,
        nombre: str,
        costo_base: float,
        especialidad: str,
        disponible: bool = True
    ):
        """
        Constructor de la clase Asesoria.
        """
        super().__init__(nombre, costo_base, disponible)

        self.especialidad = especialidad

    # ==================================================
    # Especialidad
    # ==================================================

    @property
    def especialidad(self) -> str:
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor: str):
        """
        Valida la especialidad.
        """

        if not valor.strip():
            raise ParametroInvalidoError(
                "Debe indicar una especialidad."
            )

        self._especialidad = valor.title()

    # ==================================================
    # Polimorfismo
    # ==================================================

    def calcular_costo(
        self,
        horas: int,
        descuento: float = 0.0,
        impuesto: float = 0.0
    ) -> float:
        """
        Calcula el costo de la asesoría.

        Args:
            horas: Duración de la asesoría.
            descuento: Descuento opcional.
            impuesto: Impuesto opcional.

        Returns:
            float
        """

        if horas <= 0:
            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )

        total = self.costo_base * horas

        # Recargo del 15 % por asesoría especializada
        total *= 1.15

        if descuento > 0:
            total -= total * (descuento / 100)

        if impuesto > 0:
            total += total * (impuesto / 100)

        return round(total, 2)

    # ==================================================

    def descripcion(self) -> str:
        """
        Devuelve la descripción del servicio.
        """

        return (
            f"Asesoría especializada en "
            f"{self.especialidad}."
        )

    # ==================================================

    def mostrar_informacion(self) -> str:
        """
        Devuelve la información del servicio.
        """

        estado = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        return (
            f"\n========== SERVICIO ==========\n"
            f"Nombre        : {self.nombre}\n"
            f"Especialidad  : {self.especialidad}\n"
            f"Costo Base    : ${self.costo_base:,.2f}\n"
            f"Estado        : {estado}\n"
        )

    # ==================================================

    def __str__(self) -> str:
        """
        Representación en texto del objeto.
        """

        return (
            f"{self.nombre} - "
            f"{self.especialidad}"
        )