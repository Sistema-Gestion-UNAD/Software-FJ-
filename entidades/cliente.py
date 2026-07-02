"""
---------------------------------------------------------
Archivo: cliente.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
    Clase que representa un cliente del sistema.
---------------------------------------------------------
"""

import re

from entidades.entidad import Entidad
from excepciones.excepciones import ClienteInvalidoError


class Cliente(Entidad):
    """
    Representa un cliente registrado en el sistema.
    """

    def __init__(
        self,
        nombre: str,
        documento: str,
        correo: str
    ):
        """
        Constructor de la clase Cliente.
        """
        super().__init__()

        self.nombre = nombre
        self.documento = documento
        self.correo = correo

    # ==================================================
    # Nombre
    # ==================================================

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):

        if not isinstance(valor, str):
            raise ClienteInvalidoError(
                "El nombre debe ser una cadena de texto."
            )

        valor = valor.strip()

        if len(valor) < 3:
            raise ClienteInvalidoError(
                "El nombre debe contener al menos 3 caracteres."
            )

        self._nombre = valor.title()

    # ==================================================
    # Documento
    # ==================================================

    @property
    def documento(self) -> str:
        return self._documento

    @documento.setter
    def documento(self, valor: str):

        valor = str(valor).strip()

        if not valor.isdigit():
            raise ClienteInvalidoError(
                "El documento solo debe contener números."
            )

        if len(valor) < 6:
            raise ClienteInvalidoError(
                "El documento debe tener al menos 6 dígitos."
            )

        self._documento = valor

    # ==================================================
    # Correo
    # ==================================================

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str):

        valor = valor.strip().lower()

        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(patron, valor):
            raise ClienteInvalidoError(
                "El correo electrónico no es válido."
            )

        self._correo = valor

    # ==================================================
    # Información
    # ==================================================

    def mostrar_informacion(self) -> str:
        """
        Devuelve la información del cliente.
        """

        return (
            "\n========== CLIENTE ==========\n"
            f"ID         : {self.id}\n"
            f"Nombre     : {self.nombre}\n"
            f"Documento  : {self.documento}\n"
            f"Correo     : {self.correo}\n"
            f"Registro   : "
            f"{self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

    # ==================================================

    def __str__(self) -> str:
        """
        Representación en texto del cliente.
        """

        return (
            f"{self.nombre} "
            f"({self.documento})"
        )