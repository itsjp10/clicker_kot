import serial
import time

# Cambia COM3 por tu puerto
arduino = serial.Serial('COM4', 9600)
time.sleep(2)  # Espera que Arduino se reinicie

click_times = [0.1, 0.5, 1.05, 0.7, 1.6, 1.7, 1.7, 1.58, 0.86, 0.9, 0.77, 0.5] #base Jeanpi https://www.youtube.com/watch?v=Yo2iAWjP3Ug&t=45s&ab_channel=g3cd
click_times = [0.1, 0.3, 0.3, 1.65] #base con dos plataformas salto milimetrico sin trampas
click_times = [1, 0.15, 0.13, 18.6, 0.23, 1.53, 0.53, 0.66, 1.33, 0.46, 0.96] #

for t in click_times:
    time.sleep(t)
    arduino.write(b'CLICK\n')
    print(f"CLICK enviado después de {t} segundos")

arduino.close()
