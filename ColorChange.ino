int PIN = A0;            //analog pin connected to potentiometer
unsigned int SIG = 0;    //unsigned int to be able to contain 0-65535 (0xffff) (2 bytes)

void setup() {
  Serial.begin(9600);    //common baud rate for arduino
  pinMode(PIN,INPUT);    // set analog pin as an input
}

void loop() {
   SIG = analogRead(PIN);     //read analog pin
   SIG = map(SIG, 0, 1023, 0, 65535);  // Scale potentiometer values to hex values
   Serial.println(SIG);    // print scaled signal values to serial
}
