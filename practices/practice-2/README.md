# Práctica Calificada Nº 2
***Administración de Redes (CC 312)***

## Parte 1: Ejecutar la máquina virtual (Virtual Machine) de DEVASC.

![alt text](image.png)

## Parte 2: Verificar la conectividad externa con el Packet Tracer


### Paso 1: Abriendo Packet Tracer

Primero inicié sesión en Packet Tracer
![alt text](image-1.png)


Luego descargué el archivo Packet Tracer - Implementar API REST con un SDN Controller.pka

![alt text](image-3.png)

![alt text](image-4.png)

Entrando...

![alt text](image-5.png)

### Paso 2: Verifique la configuración de Packet Tracer para el acceso externo.

Viendo que esté habilitado el acceso externo con Rest API

![alt text](image-6.png)

Chequeando acceso para el controlador

![alt text](image-7.png)

### Paso 3: Compruebe que puede acceder a Packet Tracer desde otro programa en la VM DEVASC.

![alt text](image-8.png)


## Parte 3: Solicitar un token de autenticación con Postman

Entrando a la documentación de la API REST para el controlador
![alt text](image-10.png)
![alt text](image-11.png)
![alt text](image-12.png)

También desde Help -> Context

![alt text](image-13.png)

Adding a new request

![alt text](image-14.png)

Usaremos el método POST
```
curl -X POST "http://{IP}:{PORT}/ticket"
```

#### Entrando a Postman
Iniciando sesión en Postman
![alt text](image-2.png)

![alt text](image-9.png)

Seteando el request
 ![alt text](image-15.png)

Pasando el body a raw -> JSON
![alt text](image-16.png)

Agregando el payload

![alt text](image-17.png)

La respuesta:
![alt text](image-18.png)

El ticket que me dió:
```
NC-147-ef90d57dafa942649519-nbi
```
## Parte 4: Enviar solicitudes REST con Postman

Creando nueva solicitud en Postman apuntando a http://localhost:58000/api/v1/network-device y agreando el ticket en el header como X-Auth-Token con el valor del ticket obtenido anteriormente.

![alt text](image-19.png)


Después de enviar la solicitud, se mostró el siguiente resultado:
![alt text](image-20.png)

Observo que se obtuvo el listado de dispositivos de red y toda la topología de la red, lo cual incluye cómo se conectan los dispositivos entre sí. Noté que se corresponden con los dispositivos que se ven en el Packet Tracer.

```
{
    "response": [
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet0/0/0",
                "GigabitEthernet0",
                "FastEthernet0"
            ],
            "connectedNetworkDeviceIpAddress": [
                "192.168.101.1",
                "192.168.101.254",
                "192.168.101.100"
            ],
            "connectedNetworkDeviceName": [
                "R1",
                "NetworkController",
                "Example Server"
            ],
            "errorDescription": "",
            "globalCredentialId": "53046ecc-88c3-49f6-9626-ca8ab9db6725",
            "hostname": "SWL1",
            "id": "CAT1010BT47-uuid",
            "interfaceCount": "29",
            "inventoryStatusDetail": "Managed",
            "lastUpdateTime": "11",
            "lastUpdated": "2020-06-11 18:19:42",
            "macAddress": "000C.CF42.2B11",
            "managementIpAddress": "192.168.101.2",
            "platformId": "3650",
            "productId": "3650-24PS",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "CAT1010BT47-",
            "softwareVersion": "16.3.2",
            "type": "MultiLayerSwitch",
            "upTime": "19 minutes, 2 seconds"
        },
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet1/0/1",
                "Serial0/1/0"
            ],
            "connectedNetworkDeviceIpAddress": [
                "192.168.101.2",
                "192.168.1.1"
            ],
            "connectedNetworkDeviceName": [
                "SWL1",
                "R3"
            ],
            "errorDescription": "",
            "globalCredentialId": "53046ecc-88c3-49f6-9626-ca8ab9db6725",
            "hostname": "R1",
            "id": "FDO1302XY2X-uuid",
            "interfaceCount": "6",
            "inventoryStatusDetail": "Managed",
            "ipAddresses": [
                "192.168.101.1",
                "192.168.1.2"
            ],
            "lastUpdateTime": "11",
            "lastUpdated": "2020-06-11 18:19:42",
            "macAddress": "00D0.5852.527D",
            "managementIpAddress": "192.168.1.2",
            "platformId": "ISR4300",
            "productId": "ISR4331",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "FDO1302XY2X-",
            "softwareVersion": "15.4",
            "type": "Router",
            "upTime": "19 minutes, 2 seconds"
        },
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet1/0/1",
                "GigabitEthernet1/0/1",
                "Serial0/1/0",
                "Serial0/1/1"
            ],
            "connectedNetworkDeviceIpAddress": [
                "10.0.1.2",
                "",
                "192.168.1.2",
                "192.168.2.2"
            ],
            "connectedNetworkDeviceName": [
                "SWR1",
                "SWR2",
                "R1",
                "R2"
            ],
            "errorDescription": "",
            "globalCredentialId": "53046ecc-88c3-49f6-9626-ca8ab9db6725",
            "hostname": "R3",
            "id": "FDO13026087-uuid",
            "interfaceCount": "6",
            "inventoryStatusDetail": "Managed",
            "ipAddresses": [
                "10.0.1.1",
                "10.0.2.1",
                "192.168.1.1",
                "192.168.2.1"
            ],
            "lastUpdateTime": "11",
            "lastUpdated": "2020-06-11 18:19:42",
            "macAddress": "00E0.B039.A39C",
            "managementIpAddress": "192.168.2.1",
            "platformId": "ISR4300",
            "productId": "ISR4331",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "FDO13026087-",
            "softwareVersion": "15.4",
            "type": "Router",
            "upTime": "19 minutes, 2 seconds"
        },
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet0/0/0",
                "GigabitEthernet1/0/2",
                "GigabitEthernet1/0/3",
                "GigabitEthernet1/0/5"
            ],
            "connectedNetworkDeviceIpAddress": [
                "10.0.1.1",
                "10.0.1.4",
                "10.0.1.5",
                "10.0.1.3"
            ],
            "connectedNetworkDeviceName": [
                "R3",
                "SWR3",
                "SWR4",
                "SWR2"
            ],
            "errorDescription": "",
            "globalCredentialId": "53046ecc-88c3-49f6-9626-ca8ab9db6725",
            "hostname": "SWR1",
            "id": "CAT101021Z6-uuid",
            "interfaceCount": "29",
            "inventoryStatusDetail": "Managed",
            "lastUpdateTime": "11",
            "lastUpdated": "2020-06-11 18:19:42",
            "macAddress": "00E0.F915.E250",
            "managementIpAddress": "10.0.1.2",
            "platformId": "3650",
            "productId": "3650-24PS",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "CAT101021Z6-",
            "softwareVersion": "16.3.2",
            "type": "MultiLayerSwitch",
            "upTime": "19 minutes, 2 seconds"
        },
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet0/0/1",
                "GigabitEthernet1/0/2",
                "GigabitEthernet1/0/4",
                "GigabitEthernet1/0/5"
            ],
            "connectedNetworkDeviceIpAddress": [
                "10.0.2.1",
                "10.0.1.5",
                "10.0.1.4",
                "10.0.1.2"
            ],
            "connectedNetworkDeviceName": [
                "R3",
                "SWR4",
                "SWR3",
                "SWR1"
            ],
            "errorDescription": "",
            "globalCredentialId": "53046ecc-88c3-49f6-9626-ca8ab9db6725",
            "hostname": "SWR2",
            "id": "CAT1010JJ1H-uuid",
            "interfaceCount": "29",
            "inventoryStatusDetail": "Managed",
            "lastUpdateTime": "11",
            "lastUpdated": "2020-06-11 18:19:42",
            "macAddress": "00E0.B060.5317",
            "managementIpAddress": "10.0.1.3",
            "platformId": "3650",
            "productId": "3650-24PS",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "CAT1010JJ1H-",
            "softwareVersion": "16.3.2",
            "type": "MultiLayerSwitch",
            "upTime": "19 minutes, 2 seconds"
        },
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet1/0/1",
                "Serial0/1/1"
            ],
            "connectedNetworkDeviceIpAddress": [
                "192.168.102.2",
                "192.168.2.1"
            ],
            "connectedNetworkDeviceName": [
                "SWL2",
                "R3"
            ],
            "errorDescription": "",
            "globalCredentialId": "53046ecc-88c3-49f6-9626-ca8ab9db6725",
            "hostname": "R2",
            "id": "FDO13022UJ0-uuid",
            "interfaceCount": "6",
            "inventoryStatusDetail": "Managed",
            "ipAddresses": [
                "192.168.102.1",
                "192.168.2.2"
            ],
            "lastUpdateTime": "11",
            "lastUpdated": "2020-06-11 18:19:42",
            "macAddress": "0060.4797.3DA5",
            "managementIpAddress": "192.168.2.2",
            "platformId": "ISR4300",
            "productId": "ISR4331",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "FDO13022UJ0-",
            "softwareVersion": "15.4",
            "type": "Router",
            "upTime": "19 minutes, 2 seconds"
        },
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet0/0/0",
                "FastEthernet0"
            ],
            "connectedNetworkDeviceIpAddress": [
                "192.168.102.1",
                "192.168.102.3"
            ],
            "connectedNetworkDeviceName": [
                "R2",
                "PC4"
            ],
            "errorDescription": "",
            "globalCredentialId": "53046ecc-88c3-49f6-9626-ca8ab9db6725",
            "hostname": "SWL2",
            "id": "CAT101059L6-uuid",
            "interfaceCount": "29",
            "inventoryStatusDetail": "Managed",
            "lastUpdateTime": "11",
            "lastUpdated": "2020-06-11 18:19:42",
            "macAddress": "0090.2155.BB91",
            "managementIpAddress": "192.168.102.2",
            "platformId": "3650",
            "productId": "3650-24PS",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "CAT101059L6-",
            "softwareVersion": "16.3.2",
            "type": "MultiLayerSwitch",
            "upTime": "19 minutes, 2 seconds"
        },
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet1/0/2",
                "GigabitEthernet1/0/3",
                "GigabitEthernet1/0/5",
                "FastEthernet0",
                "FastEthernet0"
            ],
            "connectedNetworkDeviceIpAddress": [
                "10.0.1.3",
                "10.0.1.2",
                "10.0.1.4",
                "10.0.2.129",
                "10.0.2.130"
            ],
            "connectedNetworkDeviceName": [
                "SWR2",
                "SWR1",
                "SWR3",
                "PC2",
                "PC3"
            ],
            "errorDescription": "",
            "globalCredentialId": "53046ecc-88c3-49f6-9626-ca8ab9db6725",
            "hostname": "SWR4",
            "id": "CAT1010K0UR-uuid",
            "interfaceCount": "29",
            "inventoryStatusDetail": "Managed",
            "lastUpdateTime": "11",
            "lastUpdated": "2020-06-11 18:19:42",
            "macAddress": "0060.5C0D.E4AE",
            "managementIpAddress": "10.0.1.5",
            "platformId": "3650",
            "productId": "3650-24PS",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "CAT1010K0UR-",
            "softwareVersion": "16.3.2",
            "type": "MultiLayerSwitch",
            "upTime": "19 minutes, 2 seconds"
        },
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet1/0/2",
                "GigabitEthernet1/0/4",
                "GigabitEthernet1/0/5",
                "FastEthernet0",
                "FastEthernet0"
            ],
            "connectedNetworkDeviceIpAddress": [
                "10.0.1.2",
                "10.0.1.3",
                "10.0.1.5",
                "10.0.1.130",
                "10.0.1.129"
            ],
            "connectedNetworkDeviceName": [
                "SWR1",
                "SWR2",
                "SWR4",
                "Admin",
                "PC1"
            ],
            "errorDescription": "",
            "globalCredentialId": "53046ecc-88c3-49f6-9626-ca8ab9db6725",
            "hostname": "SWR3",
            "id": "CAT1010J4FO-uuid",
            "interfaceCount": "29",
            "inventoryStatusDetail": "Managed",
            "lastUpdateTime": "11",
            "lastUpdated": "2020-06-11 18:19:42",
            "macAddress": "0050.0F7C.0C09",
            "managementIpAddress": "10.0.1.4",
            "platformId": "3650",
            "productId": "3650-24PS",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "CAT1010J4FO-",
            "softwareVersion": "16.3.2",
            "type": "MultiLayerSwitch",
            "upTime": "19 minutes, 2 seconds"
        }
    ],
    "version": "1.0"
}
```

Noto los siguientes dispositivos:
- `"hostname": "R1"`
- `"hostname": "R2"`
- `"hostname": "R3"`
- `"hostname": "SWR1"`
- `"hostname": "SWR2"`
- `"hostname": "SWR3"`
- `"hostname": "SWR4"`

Con ello cerramos el Postman.


## Parte 5: Enviar solicitudes REST con código VS

Entrando a la ruta devnet-src/ptna y entrando a VSC

![alt text](image-22.png)

Ejecutando el primer script .py

![alt text](image-23.png)

Observación: El ticket que se obtiene es DIFERENTE al que se obtuvo en Postman.

![alt text](image-24.png)

Reemplazando el ticket en los otros 2 scripts .py y ejecutándolos:

![alt text](image-25.png)

Ejecutando el segundo script .py

![alt text](image-26.png)

Me otorgó la topología de la red, la cual es idéntica a la que se vió en Packet Tracer; esto incluyó la id de la plataforma y la ip de cada dispositivo.

```python
print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])
```
![alt text](image-27.png)

Usando el tercer script pude obtener la información de los hosts, incluyendo su nombre, dirección IP, dirección MAC y la interfaz a la que están conectados.
```python
print(host["hostName"], "\t", host["hostIp"], "\t", host["hostMac"], "\t", host["connectedInterfaceName"])
```

![alt text](image-28.png)



## Parte 6: Enviar solicitudes REST dentro del Packet Tracer

Entro a la pc Admin y creo un nuevo proyecto de programación con python llamado API REST.

![alt text](image-29.png)

Agregando el código del script 3 que se encuentra en devnet-src/ptna en main.py

![alt text](image-30.png)

Cambiando el localhost por la ip del controlador `192.168.101.254`

![alt text](image-32.png)

Al terminar de correr:

![alt text](image-33.png)


Ahora hacemos lo mismo para el script 2, reemplazando el localhost por la ip del controlador `192.168.101.254`

![alt text](image-34.png)

Con ello concluimos la práctica!