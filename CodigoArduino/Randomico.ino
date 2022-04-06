int numero;

void setup() {
  Serial.begin(9600);
}

void loop() {
  numero = random(100);
  Serial.println(numero);
  delay(1000);
}