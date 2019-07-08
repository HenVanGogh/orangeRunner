 
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

int literation = 0;

float offSety = 0;
float offSetz = 0;
float offSetx = 0;

float offSetLx = 0;
float offSetLy = 50;
float offSetLz = 0;

String fileName = "2019_07_02_18_59 - 2019_07_02_18_59";
Table table;
//HLine h2 = new HLine(50, 2.5);
PeasyCam cam;

public void settings() {
  size(800, 480, P3D);
  fullScreen();
}

public void setup() {
  frameRate(120);
  //fullScreen();
  cam = new PeasyCam(this, 400);
  //loadData();
  table = loadTable("2019_07_02_18_59 - 2019_07_02_18_59.csv", "header");
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
  while(offSetLy < 10){
   offSetLy++; 
  }
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
vertex(300,-200,300); 
vertex(-300,-200,300); 
vertex(-300,-200,-300); 
vertex(300,-200,-300); 
endShape(CLOSE);
  
  strokeWeight(1);
  
  //rotateX(0.523599);  
  //rotateY(0.523599);  
  //rotateZ(0.523599);  
  
    
  mech1.setPoint(offSetLx , offSetLy , offSetLz);
  mech1.setRotation(offSetx, offSety, offSetz);
  
  executeOneLine(literation);
  literation++;
  if(literation > 6136){
   literation = 0; 
  }
  
  
  /*
  mech1.setEndPoint1(200 , 0 , 200);
  mech1.setEndPoint2(-200 , 0 , 200);
  mech1.setEndPoint3(-200 , 0 , -200);
  mech1.setEndPoint4(200 , 0 , -200);
  */
  
  mech1.update();
  
  HUD(offSetx , offSety ,offSetz ,offSetLx ,offSetLy ,offSetLz);
  


}

void executeOneLine(int line){
  TableRow row = table.getRow(line);
  

  
  float radiusSqrt = 126.8095 / sqrt(2);
  
  /*
  mech1.setEndPoint1(200 , 0 , 200);
  mech1.setEndPoint2(-200 , 0 , 200);
  mech1.setEndPoint3(-200 , 0 , -200);
  mech1.setEndPoint4(200 , 0 , -200);
  */
  
  mech1.setEndPoint1(row.getFloat("Leg2_x") + radiusSqrt , -row.getFloat("Leg2_y") , row.getFloat("Leg2_z") + radiusSqrt);
  mech1.setEndPoint2(-row.getFloat("Leg1_x") - radiusSqrt , -row.getFloat("Leg1_y") , -row.getFloat("Leg1_z") + radiusSqrt);
  mech1.setEndPoint3(-row.getFloat("Leg4_x") - radiusSqrt , -row.getFloat("Leg4_y") , -row.getFloat("Leg4_z") - radiusSqrt);
  mech1.setEndPoint4(row.getFloat("Leg3_x") + radiusSqrt , -row.getFloat("Leg3_y") , row.getFloat("Leg3_z") - radiusSqrt);
  
  /*
  mech1.setEndPoint1(row.getFloat("Leg2_x") + radiusSqrt , -row.getFloat("Leg2_y") , row.getFloat("Leg2_z") + radiusSqrt);
  mech1.setEndPoint2(-row.getFloat("Leg1_x") - radiusSqrt , -row.getFloat("Leg1_y") , row.getFloat("Leg1_z") + radiusSqrt);
  mech1.setEndPoint3(-row.getFloat("Leg4_x") - radiusSqrt , -row.getFloat("Leg4_y") , -row.getFloat("Leg4_z") - radiusSqrt);
  mech1.setEndPoint4(row.getFloat("Leg3_x") + radiusSqrt , -row.getFloat("Leg3_y") , -row.getFloat("Leg3_z") - radiusSqrt);
  */
}
