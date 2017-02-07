import zeep
import requests
from zeep.wsse.signature import Signature
from zeep.transports import Transport


#CABECERAS FACTURAS
cabecera = {
	"IDVersionSii":0.5,
	"Titular":{
		"NombreRazon":"NOMBRE EMPRESA EMISORA",
		"NIF":"XXXXXXXXX"},
	"TipoComunicacion":"A0"}

#FACTURAS
facturas={
	"IDFactura":{
		"IDEmisorFactura":{
			"NIF":"XXXXXXXXX"
			},
		"NumSerieFacturaEmisor":"ID factura",
		"FechaExpedicionFacturaEmisor":"16/01/2017"},
	"PeriodoImpositivo":{
		"Ejercicio":"2017",
		"Periodo":"01"
		},
	"FacturaExpedida":{
		"TipoFactura":"F1",
		"ClaveRegimenEspecialOTrascendencia":"01",
		"DescripcionOperacion":"123",
		"Contraparte":{
			"NombreRazon":"Nombre destinatario",
			"NIF":"B12463220"},
		"TipoDesglose":{
			"DesgloseFactura":{
				"Sujeta":{
					"NoExenta":{
						"TipoNoExenta":"S1",
				   		"DesgloseIVA":{
							"DetalleIVA":{
							"TipoImpositivo":21,
							"BaseImponible":22.07,
							"CuotaRepercutida":4.63,
							"TipoRecargoEquivalencia":0,
							"CuotaRecargoEquivalencia":0
							}
						}
					}
				}
	          	 }
		}
	}	
}

#WEBSERVICE AEAT
wsdl = 'http://www.agenciatributaria.es/static_files/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Modelos_y_formularios/Suministro_inmediato_informacion/FicherosSuministros/V_05/SuministroFactEmitidas.wsdl'
# Descargar los wsdl de la aeat y modificar la url del servicio por la del servicio de pruebas ya que si no te manda a XXXX

#SSL CONECTION
session = requests.Session()
session.cert='DIRECCION CLAVE PRIVADA .pem'
transport = Transport(session=session)
#FIRMA XML ENVIO
signature = Signature("DIRECCION CLAVE PRIVADA .pem","DIRECCION CLAVE PUBLICA.crt")
client = zeep.Client(wsdl=wsdl,wsse=signature,transport=transport)
#SELECCION SERVICIO DE PRUEBAS
service2 = client.bind('siiService', 'SuministroFactEmitidasPruebas')
#INSERCION DE LA FACTURA Y RESPUESTA EN EL SERVICO DE PRUEBAS.
print (service2.SuministroLRFacturasEmitidas(cabecera,facturas))

#INSERCION DE LA FACTURA Y RESPUESTA EN EL SERVICO.
#print (client.service.SuministroLRFacturasEmitidas(cabecera,facturas))


	
