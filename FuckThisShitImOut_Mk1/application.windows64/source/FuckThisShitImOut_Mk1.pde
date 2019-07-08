 
import peasy.PeasyCam;
int ID = 0;
int IDlimit = 99;
float[][] tableV = new float[5][4];
  
int[] numbers = new int[3];
boolean loopV = true;

float preset1 = 150;
float preset2 = 150;

int select;

float time = 0;

float offSety = 0;
float offSetz = 0;
float offSetx = 0;

float offSetLx = 0;
float offSetLy = 50;
float offSetLz = 0;


//HLine h2 = new HLine(50, 2.5);
PeasyCam cam;

public void settings() {
  size(1366, 768, P3D);
}

public void setup() {
  fullScreen();
  cam = new PeasyCam(this, 400);
  
}

void keyPressed() {
if(key == 'a'){
  IDlimit = IDlimit-1;
}

if(key == 'q'){
  IDlimit = IDlimit+1;
}

if(key == 'A'){
  select = 1;
}
if(key == 'B'){
  select = 2;
}
if(key == 'C'){
  select = 3;
}
if(key == 'D'){
  select = 4;
}
if(key == 'E'){
  select = 5;
}

if(key == 'a'){
  offSety = offSety-0.10;
}

if(key == 'q'){
  offSety = offSety+0.10;
}

if(key == 's'){
  offSetx = offSetx-0.10;
}

if(key == 'w'){
  offSetx = offSetx+0.10;
}

if(key == 'd'){
  offSetz = offSetz-0.10;
}

if(key == 'e'){
  offSetz = offSetz+0.10;
}




if(key == 'f'){
  offSetLy = offSetLy-10.00;
}

if(key == 'r'){
  offSetLy = offSetLy+10.00;
}

if(key == 'g'){
  offSetLx = offSetLx-10.00;
}

if(key == 't'){
  offSetLx = offSetLx+10.00;
}

if(key == 'h'){
  offSetLz = offSetLz-10.00;
}

if(key == 'y'){
  offSetLz = offSetLz+10.00;
}
}
public void draw() {
    strokeWeight(3);
  ID = 0;
  loopV =true;
  background(190);
  

  stroke(255);
  fill(70);
  beginShape(); 
vertex(300,0,300); 
vertex(-300,0,300); 
vertex(-300,0,-300); 
vertex(300,0,-300); 
endShape(CLOSE);
  
  strokeWeight(1);
  
  
  
  mech1.setPoint(offSetLx , offSetLy , offSetLz);
  mech1.setRotation(offSetx , offSety , offSetz);
  
  mech1.setEndPoint1(200 , 0 , 200);
  mech1.setEndPoint2(-200 , 0 , 200);
  mech1.setEndPoint3(-200 , 0 , -200);
  mech1.setEndPoint4(200 , 0 , -200);
  
  mech1.update();
  
  
  HUD(offSetx , offSety ,offSetz ,offSetLx ,offSetLy ,offSetLz);


}



void HUD(float x ,float y ,float z , float Ax ,float Ay ,float Az){
    cam.beginHUD();
      strokeWeight(1);
   stroke(128);
  fill(0, 128);
  rect(0, 0, 70, 30);
  
  rect(0, 30, 170, 70);
  fill(255);
  text("" + nfc(frameRate, 2), 10, 18);
  text(" xAngle - " + round(x * 57.2958), 10, 41);
  text(" yAngle - " + round(y * 57.2958), 10, 52);
  text(" zAngle - " + round(z * 57.2958), 10, 63);
  
  text(" xDistance - " + round(Ax), 10, 74);
  text(" yDistance - " + round(Ay), 10, 85);
  text(" zDistance - " + round(Az), 10, 96);
  
  cam.endHUD();
}