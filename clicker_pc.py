import serial
import time

# Cambia COM3 por tu puerto
arduino = serial.Serial('COM4', 9600)
time.sleep(2)  # Espera que Arduino se reinicie

click_times = [0.1, 0.5, 1.05, 0.7, 1.6, 1.7, 1.7, 1.66, 0.86, 0.87, 0.705, 0.3]

for t in click_times:
    time.sleep(t)
    arduino.write(b'CLICK\n')
    print(f"CLICK enviado después de {t} segundos")

arduino.close()
