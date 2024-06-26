import requests

class Errors():

    def check_request(self,error):
        status_codes = {
        100: "Continuar",
        101: "Cambio de protocolo",
        102: "Procesando",
        103: "Pausa",
        200: "OK",
        201: "Creado",
        202: "Aceptado",
        203: "Información no autoritativa",
        204: "Sin contenido",
        205: "Restablecer contenido",
        206: "Contenido parcial",
        207: "Estado Multi-Status",
        208: "Ya informado",
        226: "IM Usado",
        300: "Múltiples opciones",
        301: "Movido permanentemente",
        302: "Encontrado",
        303: "Ver otro",
        304: "No modificado",
        305: "Usar proxy",
        306: "Proxy Switch",
        307: "Redirección temporal",
        308: "Redirección permanente",
        400: "Solicitud incorrecta",
        401: "No autorizado",
        402: "Pago requerido",
        403: "Prohibido",
        404: "No encontrado",
        405: "Método no permitido",
        406: "No aceptable",
        407: "Autenticación de proxy requerida",
        408: "Tiempo de espera de solicitud",
        409: "Conflicto",
        410: "Desaparecido",
        411: "Longitud requerida",
        412: "Falló la condición previa",
        413: "Entidad demasiado grande",
        414: "URI demasiado larga",
        415: "Tipo de medio no soportado",
        416: "Rango solicitado no satisfactorio",
        417: "Falló la expectativa",
        418: "Soy una tetera",
        421: "Demanda incorrecta",
        422: "Entidad no procesable",
        423: "Bloqueado",
        424: "Fallo de dependencia",
        425: "Demasiadas solicitudes",
        426: "Actualización requerida",
        428: "Requerido condicional",
        429: "Demasiadas solicitudes",
        431: "Campos de encabezado de solicitud demasiado grandes",
        444: "Sin respuesta",
        451: "No disponible por razones legales",
        499: "Cliente cerró la conexión",
        500: "Error interno del servidor",
        501: "No implementado",
        502: "Puerta de enlace incorrecta",
        503: "Servicio no disponible",
        504: "Tiempo de espera de la puerta de enlace",
        505: "Versión de HTTP no compatible",
        506: "Variante también negocia",
        507: "Espacio insuficiente en el almacenamiento",
        508: "Bucle de detección",
        510: "No extendido",
        511: "Autenticación de red requerida"
    }
        error_msg = status_codes[error]
        return print(error_msg)