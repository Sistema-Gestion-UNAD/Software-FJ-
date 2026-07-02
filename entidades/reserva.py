"""
---------------------------------------------------------
Archivo: reserva.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
    Clase que representa una reserva realizada por un
    cliente para un servicio.
---------------------------------------------------------
"""

from enum import Enum

from entidades.entidad import Entidad
from entidades.cliente import Cliente
from servicios.servicio import Servicio

from excepciones.excepciones import (
    ReservaError,
    DuracionInvalidaError
)

from utilidades.logger import Logger


class EstadoReserva(Enum):
    """
    Estados posibles de una reserva.
    """
    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"


class Reserva(Entidad):
    """
    Representa una reserva realizada por un cliente.
    """

    def __init__(
        self,
        cliente: Cliente,
        servicio: Servicio,
        duracion: int
    ):
        super().__init__()

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = EstadoReserva.PENDIENTE

    # ==================================================
    # Cliente
    # ==================================================

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):

        if not isinstance(valor, Cliente):
            raise ReservaError(
                "Debe proporcionar un objeto Cliente."
            )

        self._cliente = valor

    # ==================================================
    # Servicio
    # ==================================================

    @property
    def servicio(self):
        return self._servicio

    @servicio.setter
    def servicio(self, valor):

        if not isinstance(valor, Servicio):
            raise ReservaError(
                "Debe proporcionar un objeto Servicio."
            )

        self._servicio = valor

    # ==================================================
    # Duración
    # ==================================================

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):

        if valor <= 0:
            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )

        self._duracion = valor

    # ==================================================
    # Confirmar Reserva
    # ==================================================

    def confirmar(self):
        """
        Confirma la reserva.
        """

        try:

            self.servicio.validar_disponibilidad()

            self.estado = EstadoReserva.CONFIRMADA

        except Exception as error:

            Logger.error(str(error))

            raise ReservaError(
                "Error al confirmar la reserva."
            ) from error

        else:

            Logger.info(
                f"Reserva confirmada para {self.cliente.nombre}"
            )

        finally:

            Logger.info(
                "Finalizó el proceso de confirmación."
            )

    # ==================================================
    # Cancelar Reserva
    # ==================================================

    def cancelar(self):
        """
        Cancela la reserva.
        """

        self.estado = EstadoReserva.CANCELADA

        Logger.warning(
            f"Reserva cancelada para {self.cliente.nombre}"
        )

    # ==================================================
    # Procesar Reserva
    # ==================================================

    def procesar(
        self,
        descuento: float = 0.0,
        impuesto: float = 0.0
    ):
        """
        Procesa la reserva y calcula el costo.
        """

        try:

            self.confirmar()

            costo = self.servicio.calcular_costo(
                self.duracion,
                descuento,
                impuesto
            )

        except Exception as error:

            Logger.error(str(error))

            raise ReservaError(
                "No fue posible procesar la reserva."
            ) from error

        else:

            Logger.info(
                f"Reserva procesada correctamente para {self.cliente.nombre}"
            )

            return costo

        finally:

            Logger.info(
                "Proceso de reserva finalizado."
            )

    # ==================================================
    # Información
    # ==================================================

    def mostrar_informacion(self):

        return (
            "\n========== RESERVA ==========\n"
            f"Cliente : {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion} hora(s)\n"
            f"Estado  : {self.estado.value}\n"
        )

    # ==================================================

    def __str__(self):

        return (
            f"{self.cliente.nombre} | "
            f"{self.servicio.nombre} | "
            f"{self.estado.value}"
        )