"""
---------------------------------------------------------
Archivo: reserva_sala.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
    Servicio especializado para la reserva de salas.
---------------------------------------------------------
"""

from servicios.servicio import Servicio
from excepciones.excepciones import (
    DuracionInvalidaError,
    ParametroInvalidoError
)


class ReservaSala(Servicio):
    """
    Representa el servicio de reserva de salas.
    """

    def __init__(
        self,
        nombre: str,
        costo_base: float,
        capacidad: int,
        disponible: bool = True
    ):
        """
        Constructor de la clase ReservaSala.
        """
        super().__init__(
            nombre,
            costo_base,
            disponible
        )

        self.capacidad = capacidad

    # ==================================================
    # Capacidad
    # ==================================================

    @property
    def capacidad(self) -> int:
        return self._capacidad

    @capacidad.setter
    def capacidad(self, valor: int):

        if not isinstance(valor, int):
            raise ParametroInvalidoError(
                "La capacidad debe ser un número entero."
            )

        if valor <= 0:
            raise ParametroInvalidoError(
                "La capacidad debe ser mayor que cero."
            )

        self._capacidad = valor

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
        Calcula el costo de la reserva de la sala.

        Args:
            horas: Cantidad de horas reservadas.
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
            f"Reserva de sala con capacidad para "
            f"{self.capacidad} personas."
        )

    # ==================================================

    def mostrar_informacion(self) -> str:
        """
        Devuelve la información completa del servicio.
        """

        estado = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        return (
            "\n========== SERVICIO ==========\n"
            f"ID           : {self.id}\n"
            f"Nombre       : {self.nombre}\n"
            f"Costo Base   : ${self.costo_base:,.2f}\n"
            f"Capacidad    : {self.capacidad} personas\n"
            f"Estado       : {estado}\n"
            f"Descripción  : {self.descripcion()}\n"
            f"Registro     : "
            f"{self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

    # ==================================================

    def __str__(self) -> str:
        """
        Representación en texto del servicio.
        """

        return (
            f"{self.nombre} "
            f"(Capacidad: {self.capacidad})"
        )