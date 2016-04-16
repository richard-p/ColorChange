int PIN = A0;
unsigned int SIG = 0;

void setup() {
  Serial.begin(9600);
  pinMode(PIN,INPUT);
}

void loop() {
   SIG = analogRead(PIN);
   SIG = map(SIG, 0, 1023, 0, 65535);
   Serial.println(SIG);
}
