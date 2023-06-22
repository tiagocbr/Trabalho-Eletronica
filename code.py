import cv2

# Importa o classsificador das faces do dataset
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inicializa a captura de vídeo que abre a câmera padrão do computador
cap = cv2.VideoCapture(0)

# Esse loop serve para capturar os frames do vídeos
while True: 

	# Lê o próximo frame e armazena em ´img`
	_, img = cap.read()

	# O openCV naturalmente trabalha com detecção de rostos utilizando a cor padrão cinza para facilitar o processo. Essa função converte a imagem colorida do rosto em imagem cinza
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Detecta os rostos
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)

	# Desenha o retangulo em volta do rosto por meio de uma iteração
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

	# Coloca a imagem resultante na janela ´img`
	cv2.imshow('img', img)

	# Falta colocar o sinal para mandar no relé no raspberry
	
	# Para se a tecla de saida for apertada
	k = cv2.waitKey(30) & 0xff
	if k==27:
		break
cap.release()
