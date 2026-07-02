"""
---------------------------------------------------------
Archivo: gestor.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
    Clase encargada de administrar clientes,
    servicios y reservas del sistema.
---------------------------------------------------------
"""

from entidades.cliente import Cliente
from entidades.reserva import Reserva
from servicios.servicio import Servicio

from excepciones.excepciones import (
    ClienteInvalidoError,
    ReservaError,
    ParametroInvalidoError
)

from utilidades.logger import Logger


class GestorSistema:
    """
    Clase encargada de gestionar toda la información
    del sistema mediante listas en memoria.
    """

    def __init__(self):
        self._clientes = []
        self._servicios = []
        self._reservas = []

        Logger.info("Gestor del sistema inicializado.")

    # ==================================================
    # CLIENTES
    # ==================================================

    def agregar_cliente(self, cliente: Cliente):

        if not isinstance(cliente, Cliente):
            raise ClienteInvalidoError(
                "Solo es posible registrar objetos Cliente."
            )

        if self.buscar_cliente(cliente.documento) is not None:
            raise ClienteInvalidoError(
                "Ya existe un cliente con ese documento."
            )

        self._clientes.append(cliente)

        Logger.info(
            f"Cliente registrado: {cliente.nombre}"
        )

    def obtener_clientes(self):

        return self._clientes

    def buscar_cliente(self, documento: str):

        for cliente in self._clientes:

            if cliente.documento == documento:
                return cliente

        return None

    # ==================================================
    # SERVICIOS
    # ==================================================

    def agregar_servicio(self, servicio: Servicio):

        if not isinstance(servicio, Servicio):
            raise ParametroInvalidoError(
                "El objeto recibido no es un servicio."
            )

        self._servicios.append(servicio)

        Logger.info(
            f"Servicio registrado: {servicio.nombre}"
        )

    def obtener_servicios(self):

        return self._servicios

    def buscar_servicio(self, nombre: str):

        for servicio in self._servicios:

            if servicio.nombre.lower() == nombre.lower():
                return servicio

        return None

    # ==================================================
    # RESERVAS
    # ==================================================

    def agregar_reserva(self, reserva: Reserva):

        if not isinstance(reserva, Reserva):
            raise ReservaError(
                "El objeto recibido no corresponde a una reserva."
            )

        self._reservas.append(reserva)

        Logger.info(
            "Reserva registrada correctamente."
        )

    def obtener_reservas(self):

        return self._reservas

    # ==================================================
    # ESTADÍSTICAS
    # ==================================================

    def total_clientes(self):

        return len(self._clientes)

    def total_servicios(self):

        return len(self._servicios)

    def total_reservas(self):

        return len(self._reservas)

    # ==================================================
    # INFORMACIÓN
    # ==================================================

    def mostrar_estadisticas(self):

        return (
            "\n========== ESTADÍSTICAS ==========\n"
            f"Clientes registrados : {self.total_clientes()}\n"
            f"Servicios registrados: {self.total_servicios()}\n"
            f"Reservas realizadas  : {self.total_reservas()}\n"
        )