import pyautogui
import time
error_segundo = 0.02

real = [8, 8.13, 9.14, 10.07, 11.27, 13.18, 15.07, 16.24, 17.20, 18.16, 19.087, 19.2]
decimas_only = []
for i in real:
    entero = int(i)
    decimal = i - entero
    decimal = round(decimal, 2)
    decimal = decimal * 100
    decimas_entero = int(decimal)
    decimas_only.append(entero *30 +decimas_entero)

times = []
for i in range(len(decimas_only)-1):
    valor = decimas_only[i+1]-decimas_only[i]
    times.append(valor)

click_times = [1] #Para iniciar la base
count = 0
for t in times:
    segundo = t/30
    if(count == 0):
        click_times.append(segundo + error_segundo)
    else:
        click_times.append(segundo)
    count += 1

#click_times = [1, 1 + error_segundo, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
print(click_times)


start = time.perf_counter()
accumulated_time = 0

for t in click_times:
    accumulated_time += t
    target = start + accumulated_time

    while True:
        now = time.perf_counter()
        remaining = target - now
        if remaining <= 0:
            pyautogui.click()
            break
        elif remaining > 0.01:
            time.sleep(remaining - 0.005)  # Duerme casi todo
