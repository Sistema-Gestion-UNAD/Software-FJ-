"""
---------------------------------------------------------
Archivo: alquiler_equipo.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
    Servicio especializado para el alquiler de equipos.
---------------------------------------------------------
"""

from servicios.servicio import Servicio
from excepciones.excepciones import (
    DuracionInvalidaError,
    ParametroInvalidoError
)


class AlquilerEquipo(Servicio):
    """
    Representa el servicio de alquiler de equipos.
    """

    def __init__(
        self,
        nombre: str,
        costo_base: float,
        tipo_equipo: str,
        disponible: bool = True
    ):
        """
        Constructor de la clase.
        """
        super().__init__(nombre, costo_base, disponible)

        self.tipo_equipo = tipo_equipo

    # ==================================================
    # Tipo de Equipo
    # ==================================================

    @property
    def tipo_equipo(self) -> str:
        return self._tipo_equipo

    @tipo_equipo.setter
    def tipo_equipo(self, valor: str):
        """
        Valida el tipo de equipo.
        """

        if not valor.strip():
            raise ParametroInvalidoError(
                "Debe indicar el tipo de equipo."
            )

        self._tipo_equipo = valor.title()

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
        Calcula el costo del alquiler.

        Args:
            horas: Tiempo de alquiler.
            descuento: Descuento opcional.
            impuesto: Impuesto opcional.

        Returns:
            float: Valor total del servicio.
        """

        if horas <= 0:
            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )

        total = self.costo_base * horas

        # Seguro obligatorio del equipo (10%)
        total *= 1.10

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
            f"Servicio de alquiler del equipo "
            f"tipo {self.tipo_equipo}."
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
            f"Tipo Equipo   : {self.tipo_equipo}\n"
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
            f"{self.tipo_equipo}"
        )