#5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes.
#  Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
# Seu objetivo é descobrir qual interruptor controla qual lâmpada.
#  Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? 


#Não consegui fazer esse desafio sozinho, tive que estudar cada etapa no chatgpt.


import time
import random


def initialize_lights():
   
    lights = {1: 'off', 2: 'off', 3: 'off'}
    switches = {1: 'off', 2: 'off', 3: 'off'}

    
    switch_to_light = {1: random.randint(1, 3), 
                       2: random.randint(1, 3), 
                       3: random.randint(1, 3)}

   
    for switch, light in switch_to_light.items():
        if switches[switch] == 'on':
            lights[light] = 'on'
    
    return lights, switch_to_light

def find_switches(lights, switch_to_light):
  
    switches = {1: 'off', 2: 'off', 3: 'off'}
    
  
    switches[1] = 'on'
   
    time.sleep(10)
    
    
    switches[1] = 'off'
    switches[2] = 'on'
    
    
    results = {}
    
    
    for light_number in range(1, 4):
        if lights[light_number] == 'on':
            results[light_number] = 'second switch'
        else:
            
            results[light_number] = 'first switch' if light_number in switch_to_light.values() else 'third switch'
    
    return results


lights, switch_to_light = initialize_lights()


results = find_switches(lights, switch_to_light)

print("Estado das lâmpadas:", lights)
print("Mapeamento Interruptor -> Lâmpada:", switch_to_light)
print("Resultados:", results)
