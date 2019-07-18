from ChatBot import Parent
import time


Parent.SendStreamMessage('hola')
Parent.SendStreamWhisper('pepito', 'hola')
for i in range(10):
    print(Parent.GetRandom(1,6))

Parent.Log('Test', 'This is a test message')
Parent.PlaySound('holi.mp3', 100)


Parent.AddCooldown('Test', 'hola', 3)
print('Parent.IsOnCooldown', Parent.IsOnCooldown('Test', 'hola'))
print('Remaining time:', Parent.GetCooldownDuration('Test', 'hola'))
time.sleep(1)
print('Remaining time:', Parent.GetCooldownDuration('Test', 'hola'))
time.sleep(3)
print('Parent.IsOnCooldown', Parent.IsOnCooldown('Test', 'hola'))
print('Parent.IsOnCooldown', Parent.IsOnCooldown('Test', 'holooa'))

