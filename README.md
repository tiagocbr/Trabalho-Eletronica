# Economia_energia
Electronics project for the development of a camera coupled to a Raspberry Pi and a 5V arduino relay made at the University of São Paulo. This project has the function of automatically turning off a light bulb after a person leaves a certain room using computer vision programmed in Python and using the OpenCV library on the RaspBerry Pi. We use a pre-trained xml dataset. This project aims to reduce the energy consumption of people who forget to turn off the switch when leaving the room.


_inserir imagem e vídeo_

## Explicação do programa utilizado
O programa usa a biblioteca OpenCV para processar as imagens e a biblioteca 'RPi.GPIO' para controlar os pinos do Raspberry.

O modo dos pinos GPIO é configurado para o modo BCM, que é um dos esquemas de numeração de pinos suportados pelo Raspberry Pi, e o pino GPIO 18 é configurado como saída, pois será usado para controlar um relé.

O objeto cap representa a câmera padrão do computador.

Definidos esses parâmetros,o código consiste de um loop que captura e processa as imagens frame após frame.
Dentro do loop,são executados os seguintes passos para cada frame:

1 - Leitura do frame através da função cap.read().

2 - Conversão da imagem para escala de cinza para melhor funcionamento do algoritmo de detecção de rostos do openCV.

3 - Detecção de rostos: O classificador de cascata de Haar é usado para detectar os rostos na imagem em escala de cinza. A função detectMultiScale retorna as coordenadas dos retângulos delimitadores de cada rosto na forma de uma lista (x, y, w, h), onde (x, y) são as coordenadas do canto superior esquerdo e (w, h) são a largura e a altura do retângulo .
Nessa função, passamos como parâmetro os valores 1.1 e 4,esses parâmetros se relacionam com as características dos rostos que se deseja detectar.
Os valores foram escolhidos de forma a obter o equilíbrio adequado entre sensibilidade e precisão na detecção de rostos,também foi considerada a necessidade de desempenho do sistema.

4 - Desenho dos retângulos ao redor dos rostos : A função cv2.rectangle() é usada para desenhar o retângulo, especificando as coordenadas do canto superior esquerdo, as coordenadas do canto inferior direito, a cor (no formato BGR) e a espessura da linha.

5 - Se pelo menos um rosto for detectado, o pino GPIO é definido como nível alto, ativando assim o relé conectado a ele.

6 - A imagem resultante com os retângulos desenhados é exibida na janela 'img'.

7 - Verificação da tecla de saída : Se a tecla 'Esc' for pressionada (código ASCII 27), o loop é interrompido e o programa é encerrado.



Após sair do loop, a captura de vídeo é liberada e os pinos GPIO são limpos.

## Tabela dos componentes utiliados

| Quantidade  | Componente | Especificações  | Valor em reais |
| ------------- | ------------- | ------------- | ------------- |
| 1  | Raspberry Pi  | 4Gb RAM | Emprestada |
| 1 | Câmera | Ov5647 | Emprestada  |
| 1  | Relé | 5V | 4,85 |
| 1  | Resistor | inserir  | 0,07  |
| 1  | Transistor | NPN BC337 | 0,68  |
|  |  |  | Total: R$ 5,60 |

## Membros do grupo:
* Bruno Kazuya Yamato Sakji
* Douglas da Fontoura Pereyra
* Henrique Vilela Zucoloto
* Ayrton da Costa Ganem Filho
* Tiago Chaves Bezerra Rocha


## Créditos
Queremos agradacer ao nosso grande mestre: Eduardo do Valle Simões

