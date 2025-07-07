import pyautogui
import time

# Secuencia de tiempos entre clics
click_times = [1, 0.15, 0.13, 18.6, 0.23, 1.53, 0.53, 0.66, 1.33, 0.46, 0.96]

for t in click_times:
    time.sleep(t)
    pyautogui.click()  # Clic en la posición actual
    print(f"CLICK enviado después de {t} segundos")
