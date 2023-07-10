import cv2
import RPi.GPIO as GPIO
import time

# Importa o classificador das faces do dataset
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Configuração dos pinos da Raspberry Pi
GPIO.setmode(GPIO.BCM)
relay_pin = 18  # É o pino que é ligado no relé para ser acionado

# Configura o pino do relé como saída
GPIO.setup(relay_pin, GPIO.OUT)

# Inicializa a captura de vídeo que abre a câmera padrão do computador
cap = cv2.VideoCapture(0)

# Variáveis para controle do estado do relé e contador
relay_state = False
counter = 0
delay_duration = 10  # Delay em segundos
GPIO.output(relay_pin, GPIO.LOW)

# Esse loop serve para capturar os frames do vídeos
while True: 

    # Lê o próximo frame e armazena em ´img`
    _, img = cap.read()

    # O OpenCV naturalmente trabalha com detecção de rostos utilizando a cor padrão cinza para facilitar o processo. Essa função converte a imagem colorida do rosto em imagem cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta os rostos
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Verifica se há rostos detectados
    if len(faces) > 0:
        # Se houver rostos, ativa o relé e reseta o contador
        if not relay_state:
            GPIO.output(relay_pin, GPIO.HIGH)
            relay_state = True
            counter = 0
    else:
        # Se não houver rostos
        if relay_state:
            counter += 1
            if counter > 60:
                GPIO.output(relay_pin, GPIO.LOW)
                relay_state = False

    # Desenha o retângulo em volta do rosto por meio de uma iteração
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Coloca a imagem resultante na janela ´img`
    cv2.imshow('img', img)

    # Para se a tecla de saída for pressionada
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Libera os recursos utilizados pela câmera e pelo GPIO
cap.release()
GPIO.cleanup()
