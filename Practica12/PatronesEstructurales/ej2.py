from abc import ABC, abstractmethod

class IImpresora(ABC):
    @abstractmethod
    def imprimir(self, documento: str):
        pass

    @abstractmethod
    def escanear(self) -> str:
        pass

    @abstractmethod
    def obtener_estado(self) -> str:
        pass



    def __init__(self, puerto_usb: str):
        self._puerto_usb = puerto_usb
        print(f"Impresora USB conectada en {self._puerto_usb}")

    def imprimir_usb(self, datos_impresion: str):
        
        print(f"[USB] Imprimiendo '{datos_impresion[:20]}...' a través de {self._puerto_usb}")

    def escanear_usb(self) -> str:
       
        print(f"[USB] Escaneando documento desde {self._puerto_usb}...")
        return "Contenido escaneado por USB."

    def estado_usb(self) -> str:
        return "Lista (USB)"

class ImpresoraBluetooth:
    
    def __init__(self, mac_address: str):
        self._mac_address = mac_address
        print(f"Impresora Bluetooth conectada en {self._mac_address}")

    def enviar_datos_bt(self, datos: str):
                print(f"[Bluetooth] Enviando '{datos[:20]}...' a {self._mac_address}")

    def recibir_datos_bt(self) -> str:
        
        print(f"[Bluetooth] Recibiendo datos desde {self._mac_address}...")
        return "Documento escaneado por Bluetooth."

    def verificar_conexion_bt(self) -> str:
        
        return "Conectada (Bluetooth)"

class ImpresoraRed:

    def __init__(self, ip_address: str):
        self._ip_address = ip_address
        print(f"Impresora de Red conectada en {self._ip_address}")

    def enviar_trabajo_red(self, trabajo: str):
                print(f"[Red] Enviando trabajo '{trabajo[:20]}...' a la impresora en {self._ip_address}")

    def obtener_escaneo_red(self) -> str:

        print(f"[Red] Solicitando escaneo de la impresora en {self._ip_address}...")
        return "Imagen escaneada por Red."

    def consultar_estado_red(self) -> str:

        return "Activa (Red)"

class AdaptadorImpresoraUSB(IImpresora):
        def __init__(self, impresora_usb: ImpresoraUSB):
        self._impresora_usb = impresora_usb
        print("AdaptadorImpresoraUSB creado.")

    def imprimir(self, documento: str):
        self._impresora_usb.imprimir_usb(documento)

    def escanear(self) -> str:
        return self._impresora_usb.escanear_usb()

    def obtener_estado(self) -> str:
        return self._impresora_usb.estado_usb()

class AdaptadorImpresoraBluetooth(IImpresora):
    def __init__(self, impresora_bt: ImpresoraBluetooth):
        self._impresora_bt = impresora_bt
        print("AdaptadorImpresoraBluetooth creado.")

    def imprimir(self, documento: str):
        self._impresora_bt.enviar_datos_bt(documento)

    def escanear(self) -> str:
        return self._impresora_bt.recibir_datos_bt()

    def obtener_estado(self) -> str:
        return self._impresora_bt.verificar_conexion_bt()

class AdaptadorImpresoraRed(IImpresora):
        def __init__(self, impresora_red: ImpresoraRed):
        self._impresora_red = impresora_red
        print("AdaptadorImpresoraRed creado.")

    def imprimir(self, documento: str):
        self._impresora_red.enviar_trabajo_red(documento)

    def escanear(self) -> str:
        return self._impresora_red.obtener_escaneo_red()

    def obtener_estado(self) -> str:
        return self._impresora_red.consultar_estado_red()

class AplicacionEscritorio:
    def trabajar_con_impresora(self, impresora: IImpresora, documento_a_imprimir: str):
        print(f"\n--- Aplicación trabajando con impresora: {impresora.__class__.__name__} ---")
        print(f"Estado de la impresora: {impresora.obtener_estado()}")
        impresora.imprimir(documento_a_imprimir)
        escaneo = impresora.escanear()
        print(f"Resultado del escaneo: '{escaneo}'")
       


if __name__ == "__main__":
    aplicacion = AplicacionEscritorio()
    documento = "Reporte Mensual de Ventas y Proyecciones"

        impresora_usb_real = ImpresoraUSB("USB001")
    adaptador_usb = AdaptadorImpresoraUSB(impresora_usb_real)
    aplicacion.trabajar_con_impresora(adaptador_usb, documento)

    impresora_bt_real = ImpresoraBluetooth("00:1A:2B:3C:4D:5E")
    adaptador_bluetooth = AdaptadorImpresoraBluetooth(impresora_bt_real)
    aplicacion.trabajar_con_impresora(adaptador_bluetooth, documento)

    impresora_red_real = ImpresoraRed("192.168.1.100")
    adaptador_red = AdaptadorImpresoraRed(impresora_red_real)
    aplicacion.trabajar_con_impresora(adaptador_red, documento)

   
