import subprocess
import speedtest
import keyboard
import timeit

teste = 1
print("Informe o IP/URL de teste.")
hostname = input()

while not keyboard.is_pressed('Esc'):
    print("_________________________________________________________________________________")

    print(f'Teste numero {teste} iniciado:')
    runtime = timeit.default_timer()
    print(f'Tempo Executando: {runtime:.02f}s')
    speed_test = speedtest.Speedtest()
    results = float(speed_test.download())
    print(f'Velocidade: {results/1000:.02f}Kbps')
    print(subprocess.run(["ping", "-n", "10", hostname]).returncode)
    teste = teste + 1

    print("_________________________________________________________________________________")
