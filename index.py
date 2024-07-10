import time

def cronometro():
    input("Pressione Enter para iniciar o cronômetro.")
    start_time = time.time()
    input("Pressione Enter para parar o cronômetro.")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"Tempo decorrido: {elapsed_time:.2f} segundos")

cronometro()
