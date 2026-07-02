"""
---------------------------------------------------------
Archivo: excepciones.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
    Contiene todas las excepciones personalizadas
    utilizadas por el sistema.
---------------------------------------------------------
"""


class SistemaGestionError(Exception):
    """
    Excepción base del sistema.

    Todas las excepciones personalizadas heredan
    de esta clase.
    """

    pass


# ======================================================
# CLIENTES
# ======================================================

class ClienteInvalidoError(SistemaGestionError):
    """
    Error cuando un cliente contiene
    información inválida.
    """

    pass


# ======================================================
# SERVICIOS
# ======================================================

class ServicioNoDisponibleError(SistemaGestionError):
    """
    Error cuando un servicio no
    se encuentra disponible.
    """

    pass


class ParametroInvalidoError(SistemaGestionError):
    """
    Error cuando un parámetro
    recibido es inválido.
    """

    pass


class DuracionInvalidaError(SistemaGestionError):
    """
    Error cuando la duración
    del servicio es inválida.
    """

    pass


# ======================================================
# RESERVAS
# ======================================================

class ReservaError(SistemaGestionError):
    """
    Error relacionado con el
    procesamiento de reservas.
    """

    pass


class ReservaCanceladaError(ReservaError):
    """
    Error cuando se intenta operar
    sobre una reserva cancelada.
    """

    pass


# ======================================================
# ARCHIVOS
# ======================================================

class ArchivoError(SistemaGestionError):
    """
    Error relacionado con archivos.
    """

    pass


# ======================================================
# LOGS
# ======================================================

class LoggerError(SistemaGestionError):
    """
    Error relacionado con el sistema
    de registro de eventos.
    """

    pass