# Energy_Saving
Electronics project for the development of a camera coupled to a Raspberry Pi and a 5V Arduino relay made at the University of São Paulo. This project aims to automatically turn off a light bulb after a person leaves a certain room using computer vision programmed in Python and the OpenCV library on the Raspberry Pi. We use a pre-trained XML dataset. The goal of this project is to reduce the energy consumption of people who forget to turn off the switch when leaving the room.

## Program Explanation
The program uses the OpenCV library to process images and the 'RPi.GPIO' library to control the Raspberry Pi pins.

The GPIO pin mode is set to BCM mode, which is one of the pin numbering schemes supported by the Raspberry Pi, and GPIO pin 18 is configured as an output as it will be used to control a relay.

The cap object represents the computer's default camera.

With these parameters set, the code consists of a loop that captures and processes the frames one by one. Within the loop, the following steps are executed for each frame:

1. Reading the frame using the cap.read() function.

2. Converting the image to grayscale for better operation of the OpenCV face detection algorithm.

3. Face detection: The Haar cascade classifier is used to detect faces in the grayscale image. The detectMultiScale function returns the coordinates of bounding rectangles for each detected face in the form of a list (x, y, w, h), where (x, y) are the coordinates of the top-left corner, and (w, h) are the width and height of the rectangle. In this function, we pass the parameters 1.1 and 4, which relate to the characteristics of the faces we want to detect. The values were chosen to achieve the proper balance between sensitivity and accuracy in face detection, taking into account the system's performance requirements.

4. Drawing rectangles around the faces: The cv2.rectangle() function is used to draw the rectangle, specifying the coordinates of the top-left corner, the coordinates of the bottom-right corner, the color (in BGR format), and the line thickness.

5. If at least one face is detected, the GPIO pin is set to a high level, thus activating the relay connected to it.

6. The resulting image with the drawn rectangles is displayed in the 'img' window.

7. Checking the exit key: If the 'Esc' key is pressed (ASCII code 27), the loop is interrupted, and the program exits.

## Explanation of the Electronics Part for Sending Messages to the Switch
* In the project, when the Raspberry Pi sends a message to the pins, they create a current that exits the pin through the female wire with 3.3V (Raspberry's default). This current passes through a resistor, and then a transistor is responsible for turning on the relay, with the ground and the Raspberry (in the NPN transistor used, these components are the emitter, the base, and the collector). Thus, with the Raspberry's activation, the relay can be triggered, and the switch is activated, turning off the room's light.

## Image and Video of the Program in Action
![alt text](https://github.com/A1RT0N/Economia_energia/blob/main/WhatsApp%20Image%202023-07-09%20at%2018.45.07.jpeg).

Link Youtube: https://youtu.be/zHyO0XfReo8 

## Circuito no Tinker Cad

![alt text](https://github.com/A1RT0N/Economia_energia/blob/main/WhatsApp%20Image%202023-07-09%20at%2019.12.43.jpeg).

## Table of Used Components

| Quantity  | Component | Specifications  | Value |
| ------------- | ------------- | ------------- | ------------- |
| 1  | Raspberry Pi  | 4Gb RAM | Emprestada |
| 1 | Câmera | Ov5647 | Emprestada  |
| 1  | Relé | 5V | 4,85 |
| 1  | Resistor | inserir  | 0,07  |
| 1  | Transistor | NPN BC337 | 0,68  |
|  |  |  | Total: R$ 5,60 |

## Group Members:
* Bruno Kazuya Yamato Sakji
* Douglas da Fontoura Pereyra
* Henrique Vilela Zucoloto
* Ayrton da Costa Ganem Filho
* Tiago Chaves Bezerra Rocha


## Credits
We would like to thank our great mentor: Eduardo do Valle Simões

