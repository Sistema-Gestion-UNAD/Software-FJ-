"""
---------------------------------------------------------
Archivo: simulacion.py
Autor: Daniel Triana
Proyecto: Sistema de Gestión Software FJ

Descripción:
Simulación completa del funcionamiento del sistema.
Demuestra la gestión de clientes, servicios y reservas,
incluyendo manejo avanzado de excepciones.
---------------------------------------------------------
"""

from entidades.cliente import Cliente
from entidades.reserva import Reserva

from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria

from utilidades.gestor import GestorSistema
from utilidades.logger import Logger

from excepciones.excepciones import SistemaGestionError


def ejecutar_simulacion():
    """
    Ejecuta la simulación completa del sistema.
    """

    print("\n")
    print("=" * 70)
    print("      SISTEMA DE GESTIÓN SOFTWARE FJ")
    print("=" * 70)

    Logger.info("Inicio de la simulación.")

    gestor = GestorSistema()

    # ==================================================
    # REGISTRO DE CLIENTES
    # ==================================================

    print("\nREGISTRO DE CLIENTES")
    print("-" * 70)

    datos_clientes = [

        ("Daniel Triana", "123456789", "daniel@email.com"),

        ("María López", "987654321", "maria@email.com"),

        ("Carlos Pérez", "456123789", "carlos@email.com"),

        ("Laura Gómez", "852741963", "laura@email.com"),

        ("Pedro Ramírez", "159357258", "pedro@email.com")
    ]

    for nombre, documento, correo in datos_clientes:

        try:

            cliente = Cliente(
                nombre,
                documento,
                correo
            )

            gestor.agregar_cliente(cliente)

            print(
                f"✔ Cliente registrado -> {cliente.nombre}"
            )

        except SistemaGestionError as error:

            Logger.error(str(error))

            print(
                f"✘ {error}"
            )

    # ==================================================
    # CLIENTES INVÁLIDOS
    # ==================================================

    print("\nVALIDACIÓN DE CLIENTES INVÁLIDOS")
    print("-" * 70)

    errores = [

        ("", "111", "correo@email.com"),

        ("Juan", "ABC123", "juan@email.com"),

        ("Luis", "123123123", "correo_invalido"),

        ("Daniel Triana", "123456789", "otro@email.com")
    ]

    for nombre, documento, correo in errores:

        try:

            cliente = Cliente(
                nombre,
                documento,
                correo
            )

            gestor.agregar_cliente(cliente)

        except Exception as error:

            Logger.warning(str(error))

            print(
                f"✔ Excepción controlada -> {error}"
            )

    # ==================================================
    # CREACIÓN DE SERVICIOS
    # ==================================================

    print("\nCREACIÓN DE SERVICIOS")
    print("-" * 70)

    try:

        sala = ReservaSala(

            "Sala Ejecutiva",

            60000,

            20

        )

        gestor.agregar_servicio(sala)

        print("✔ Sala registrada")

    except Exception as error:

        Logger.error(str(error))

        print(error)

    try:

        equipo = AlquilerEquipo(

            "Video Beam",

            35000,

            "Epson PowerLite"

        )

        gestor.agregar_servicio(equipo)

        print("✔ Equipo registrado")

    except Exception as error:

        Logger.error(str(error))

        print(error)

    try:

        asesoria = Asesoria(

            "Consultoría TI",

            150000,

            "Arquitectura de Software"

        )

        gestor.agregar_servicio(asesoria)

        print("✔ Asesoría registrada")

    except Exception as error:

        Logger.error(str(error))

        print(error)

    print("\nServicios registrados correctamente.")
    
    # ==================================================
    # CREACIÓN DE RESERVAS
    # ==================================================

    print("\nCREACIÓN DE RESERVAS")
    print("-" * 70)

    clientes = gestor.obtener_clientes()
    servicios = gestor.obtener_servicios()

    # ----------------------------------------------
    # Reserva 1
    # ----------------------------------------------

    try:

        reserva1 = Reserva(
            clientes[0],
            servicios[0],
            3
        )

        costo = reserva1.procesar()

        gestor.agregar_reserva(reserva1)

    except Exception as error:

        Logger.error(str(error))

        print(f"✘ {error}")

    else:

        print(
            f"✔ Reserva creada para {reserva1.cliente.nombre}"
        )

        print(
            f"Costo total: ${costo:,.2f}"
        )

    finally:

        Logger.info("Proceso de Reserva 1 finalizado.")

    # ----------------------------------------------
    # Reserva 2 (descuento)
    # ----------------------------------------------

    try:

        reserva2 = Reserva(
            clientes[1],
            servicios[1],
            2
        )

        costo = reserva2.procesar(
            descuento=10
        )

        gestor.agregar_reserva(reserva2)

        print(
            f"\n✔ Reserva creada para {reserva2.cliente.nombre}"
        )

        print(
            f"Costo con descuento: ${costo:,.2f}"
        )

    except Exception as error:

        Logger.error(str(error))

        print(error)

    # ----------------------------------------------
    # Reserva 3 (impuesto)
    # ----------------------------------------------

    try:

        reserva3 = Reserva(
            clientes[2],
            servicios[2],
            5
        )

        costo = reserva3.procesar(
            impuesto=19
        )

        gestor.agregar_reserva(reserva3)

        print(
            f"\n✔ Reserva creada para {reserva3.cliente.nombre}"
        )

        print(
            f"Costo con impuesto: ${costo:,.2f}"
        )

    except Exception as error:

        Logger.error(str(error))

        print(error)

    # ==================================================
    # VALIDACIONES
    # ==================================================

    print("\nVALIDACIÓN DE RESERVAS")
    print("-" * 70)

    # ----------------------------------------------
    # Duración inválida
    # ----------------------------------------------

    try:

        reserva_invalida = Reserva(
            clientes[0],
            servicios[0],
            0
        )

    except Exception as error:

        Logger.warning(str(error))

        print(
            f"✔ Duración inválida detectada: {error}"
        )

    # ----------------------------------------------
    # Servicio no disponible
    # ----------------------------------------------

    try:

        servicios[2].disponible = False

        reserva_servicio = Reserva(
            clientes[3],
            servicios[2],
            2
        )

        reserva_servicio.procesar()

    except Exception as error:

        Logger.warning(str(error))

        print(
            f"✔ Servicio no disponible: {error}"
        )

    finally:

        servicios[2].disponible = True

    # ----------------------------------------------
    # Cancelar una reserva
    # ----------------------------------------------

    try:

        reserva1.cancelar()

        print(
            "\n✔ Reserva cancelada correctamente."
        )

    except Exception as error:

        Logger.error(str(error))

        print(error)

    # ----------------------------------------------
    # Cancelar nuevamente
    # ----------------------------------------------

    try:

        reserva1.cancelar()

    except Exception as error:

        Logger.warning(str(error))

        print(
            f"✔ Segunda cancelación detectada: {error}"
        )

    # ----------------------------------------------
    # Procesar una reserva cancelada
    # ----------------------------------------------

    try:

        reserva1.procesar()

    except Exception as error:

        Logger.warning(str(error))

        print(
            f"✔ Procesamiento bloqueado: {error}"
        )

    print("\nReservas procesadas correctamente.")

    # ==================================================
    # BÚSQUEDA DE CLIENTES
    # ==================================================

    print("\nBÚSQUEDA DE CLIENTES")
    print("-" * 70)

    try:

        cliente = gestor.buscar_cliente("123456789")

        if cliente is not None:

            print("\nCliente encontrado:")

            print(cliente.mostrar_informacion())

        else:

            print("Cliente no encontrado.")

    except Exception as error:

        Logger.error(str(error))

        print(error)

    # ==================================================
    # BÚSQUEDA DE SERVICIOS
    # ==================================================

    print("\nBÚSQUEDA DE SERVICIOS")
    print("-" * 70)

    try:

        servicio = gestor.buscar_servicio(
            "Sala Ejecutiva"
        )

        if servicio is not None:

            print("\nServicio encontrado:")

            print(servicio.mostrar_informacion())

        else:

            print("Servicio no encontrado.")

    except Exception as error:

        Logger.error(str(error))

        print(error)

    # ==================================================
    # LISTADO DE CLIENTES
    # ==================================================

    print("\nLISTADO DE CLIENTES")
    print("-" * 70)

    try:

        for cliente in gestor.obtener_clientes():

            print(cliente)

    except Exception as error:

        Logger.error(str(error))

        print(error)

    # ==================================================
    # LISTADO DE SERVICIOS
    # ==================================================

    print("\nLISTADO DE SERVICIOS")
    print("-" * 70)

    try:

        for servicio in gestor.obtener_servicios():

            print(servicio)

    except Exception as error:

        Logger.error(str(error))

        print(error)

    # ==================================================
    # LISTADO DE RESERVAS
    # ==================================================

    print("\nLISTADO DE RESERVAS")
    print("-" * 70)

    try:

        reservas = gestor.obtener_reservas()

        if len(reservas) == 0:

            print("No existen reservas registradas.")

        else:

            for reserva in reservas:

                print(reserva.mostrar_informacion())

    except Exception as error:

        Logger.error(str(error))

        print(error)

    # ==================================================
    # ESTADÍSTICAS DEL SISTEMA
    # ==================================================

    print("\nESTADÍSTICAS DEL SISTEMA")
    print("-" * 70)

    try:

        print(gestor.mostrar_estadisticas())

    except Exception as error:

        Logger.error(str(error))

        print(error)

    # ==================================================
    # RESUMEN GENERAL
    # ==================================================

    print("\nRESUMEN GENERAL")
    print("-" * 70)

    print(
        f"Clientes registrados : {gestor.total_clientes()}"
    )

    print(
        f"Servicios registrados: {gestor.total_servicios()}"
    )

    print(
        f"Reservas registradas : {gestor.total_reservas()}"
    )

    print("\nEl sistema continuó funcionando correctamente")
    print("a pesar de las excepciones generadas durante")
    print("la simulación.")

    Logger.info(
        "Simulación finalizada correctamente."
    )

    print("\n" + "=" * 70)
    print("        FIN DE LA SIMULACIÓN")
    print("=" * 70)