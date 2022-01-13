//os resistores devem ser ligados no polo positivo 
//pinos do Display 7 segmentos
#define segA 7
#define segB 8 
#define segC 9
#define segD 10
#define segE 11
#define segF 12
#define segG 13

//pino do LED, do botão e do potenciometro
#define pinLED 6
#define pinBotao 5
#define pot A0

//variavel que recebe a escrita da serial e variavel auxiliar
char c;
char teste = '0';

//variavel auxiliar
bool valor = 0;

//variaveis para os valores do botão e do potenciometro
int sensorPot;
int valorBotao;

void setup() {

  // Velocidade de comunicação com a porta sereal
  Serial.begin(9600);

  // Pinos do botão e do led
  pinMode(pinBotao, INPUT);
  pinMode(pinLED, OUTPUT);

  // Pinos do display 7 segmentos
  pinMode(segA,OUTPUT);
  pinMode(segB,OUTPUT);
  pinMode(segC,OUTPUT);
  pinMode(segD,OUTPUT);
  pinMode(segE,OUTPUT);
  pinMode(segF,OUTPUT);
  pinMode(segG,OUTPUT);
}

void loop() {
  // Leitura do botão e do potenciometro
  valorBotao = digitalRead(pinBotao);
  sensorPot = analogRead(pot);

  Serial.print(valorBotao);
  Serial.print(",");
  Serial.print(sensorPot/10.23);
  Serial.println("");
  
  delay(500); 
  
  // Leitura da comunicação serial do LED
  if(Serial.available() > 0){

    c = Serial.read();
    teste = c;

    if(c == 'A' && valor == 0){
      digitalWrite(pinLED,HIGH);
      valor = 1;
    }

    if(c == 'B' && valor == 1){
      digitalWrite(pinLED,LOW);
      valor = 0;
    }
  }

  // Leitura da comunicação serial do Display 7 segmentos
  if(teste == '0'){
    num_0();
  }
  if(teste == '1'){
    num_1();
  }
  if(teste == '2'){
    num_2();
  }
  if(teste == '3'){
    num_3();
  }
  if(teste == '4'){
    num_4();
  }
  if(teste == '5'){
    num_5();
  }
  if(teste == '6'){
    num_6();
  }
  if(teste == '7'){
    num_7();
  }
  if(teste == '8'){
    num_8();
  }
  if(teste == '9'){
    num_9();
  }
  
}
void num_0(){// F e E
  digitalWrite(segA, LOW);
  digitalWrite(segB, LOW);
  digitalWrite(segC, LOW);
  digitalWrite(segD, LOW);
  digitalWrite(segE, LOW);
  digitalWrite(segF, LOW);

  digitalWrite(segG, HIGH);
}
void num_1(){// F e E
  digitalWrite(segB, LOW);
  digitalWrite(segC, LOW);
  
  digitalWrite(segA, HIGH);
  digitalWrite(segD, HIGH);
  digitalWrite(segE, HIGH);
  digitalWrite(segF, HIGH);
  digitalWrite(segG, HIGH);
}
void num_2(){// A ,B, G, E e D
  digitalWrite(segA, LOW);
  digitalWrite(segB, LOW);
  digitalWrite(segD, LOW);
  digitalWrite(segE, LOW);
  digitalWrite(segG, LOW);

  digitalWrite(segF, HIGH);
  digitalWrite(segC, HIGH);
  
}
void num_3(){// A ,B, G, C e D
  digitalWrite(segA, LOW);
  digitalWrite(segB, LOW);
  digitalWrite(segD, LOW);
  digitalWrite(segC, LOW);
  digitalWrite(segG, LOW);

  digitalWrite(segF, HIGH);
  digitalWrite(segE, HIGH);
  
}
void num_4(){// B, G, C e F
  digitalWrite(segB, LOW);
  digitalWrite(segG, LOW);
  digitalWrite(segC, LOW);
  digitalWrite(segF, LOW);

  digitalWrite(segA, HIGH);
  digitalWrite(segD, HIGH);
  digitalWrite(segE, HIGH);
  
}
void num_5(){// A, C, D, F e G
  digitalWrite(segA, LOW);
  digitalWrite(segC, LOW);
  digitalWrite(segD, LOW);
  digitalWrite(segF, LOW);
  digitalWrite(segG, LOW);

  digitalWrite(segB, HIGH);
  digitalWrite(segE, HIGH);
}
void num_6(){// A, C, D, E, F e G
  digitalWrite(segA, LOW);
  digitalWrite(segC, LOW);
  digitalWrite(segD, LOW);
  digitalWrite(segE, LOW);
  digitalWrite(segF, LOW);
  digitalWrite(segG, LOW);

  digitalWrite(segB, HIGH);
}
void num_7(){//A, B e C
  digitalWrite(segA, LOW);
  digitalWrite(segB, LOW);
  digitalWrite(segC, LOW);
  
  digitalWrite(segD, HIGH);
  digitalWrite(segE, HIGH);
  digitalWrite(segF, HIGH);
  digitalWrite(segG, HIGH);
}
void num_8(){// A ,B, C, D, E, F e G
  digitalWrite(segA, LOW);
  digitalWrite(segB, LOW);
  digitalWrite(segC, LOW);
  digitalWrite(segD, LOW);
  digitalWrite(segE, LOW);
  digitalWrite(segF, LOW);
  digitalWrite(segG, LOW);
}
void num_9(){// A ,B, C, D, F e G
  digitalWrite(segA, LOW);
  digitalWrite(segB, LOW);
  digitalWrite(segC, LOW);
  digitalWrite(segD, LOW);
  digitalWrite(segF, LOW);
  digitalWrite(segG, LOW);

  digitalWrite(segE, HIGH);
}
