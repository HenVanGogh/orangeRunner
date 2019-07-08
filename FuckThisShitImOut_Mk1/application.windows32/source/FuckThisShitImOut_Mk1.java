import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import peasy.PeasyCam; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class FuckThisShitImOut_Mk1 extends PApplet {

 

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
  
  cam = new PeasyCam(this, 400);
  
}

public void keyPressed() {
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
  offSety = offSety-0.10f;
}

if(key == 'q'){
  offSety = offSety+0.10f;
}

if(key == 's'){
  offSetx = offSetx-0.10f;
}

if(key == 'w'){
  offSetx = offSetx+0.10f;
}

if(key == 'd'){
  offSetz = offSetz-0.10f;
}

if(key == 'e'){
  offSetz = offSetz+0.10f;
}




if(key == 'f'){
  offSetLy = offSetLy-10.00f;
}

if(key == 'r'){
  offSetLy = offSetLy+10.00f;
}

if(key == 'g'){
  offSetLx = offSetLx-10.00f;
}

if(key == 't'){
  offSetLx = offSetLx+10.00f;
}

if(key == 'h'){
  offSetLz = offSetLz-10.00f;
}

if(key == 'y'){
  offSetLz = offSetLz+10.00f;
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



public void HUD(float x ,float y ,float z , float Ax ,float Ay ,float Az){
    cam.beginHUD();
      strokeWeight(1);
   stroke(128);
  fill(0, 128);
  rect(0, 0, 70, 30);
  
  rect(0, 30, 170, 70);
  fill(255);
  text("" + nfc(frameRate, 2), 10, 18);
  text(" xAngle - " + round(x * 57.2958f), 10, 41);
  text(" yAngle - " + round(y * 57.2958f), 10, 52);
  text(" zAngle - " + round(z * 57.2958f), 10, 63);
  
  text(" xDistance - " + round(Ax), 10, 74);
  text(" yDistance - " + round(Ay), 10, 85);
  text(" zDistance - " + round(Az), 10, 96);
  
  cam.endHUD();
}
class Leg {
  
  float[][] pos = new float[3][4];
  float[][] drawPos = new float[5][4];
  int[] Color = new int[4];
  float limb0 ,limb1 , limb2;
  int lineD;
  
Leg(float Limb0 ,float Limb1 , float Limb2,int lineColor1,int lineColor2,int lineColor3, int dense){
  limb1 = Limb1;
  limb2 = Limb2;
  limb0 = Limb0;
  Color[1] = lineColor1;
  Color[2] = lineColor2;
  Color[3] = lineColor3;
  lineD = dense;
}

public void setBeginningPoint(float x , float y , float z){
  pos[1][1] = x;
  pos[1][2] = y;
  pos[1][3] = z;
}

public void setEndgPoint(float x , float y , float z){
  pos[2][1] = x;
  pos[2][2] = y;
  pos[2][3] = z;
}

public void update(float why){
  
  
  float xb = abshypot(pos[2][1] - pos[1][1] , pos[2][3] - pos[1][3]);
  float L1 = xb - limb0;
  float L2 = hypot(L1 , pos[2][2] - pos[1][2]);
//float K1 = cosine(limb1 , L2 , limb2);
  float K2 = cosine(limb2 , L2 , limb1);
  float K3 = cos(L1/L2);
  float K4 = K2 + K3;
  float L3 = sin(K4) * limb2;
  float L4 = cos(K4) * limb2;
  //float K5 = sin(time);
  float K5 = atan(pos[2][3] / pos[2][1] );
  float L5 = xb - L4;
  
  drawPos[1][1] = pos[1][1];
  drawPos[1][2] = pos[1][2];
  drawPos[1][3] = pos[1][3];
      
  drawPos[2][1] = (why *cos(K5) * limb0) + pos[1][1];
  drawPos[2][2] = pos[1][2];
  drawPos[2][3] = (why *sin(K5) * limb0) + pos[1][3];
  
  drawPos[3][1] = (why *cos(K5) * L5) + pos[1][1];
  drawPos[3][2] = L3;
  drawPos[3][3] = (why *sin(K5) * L5) + pos[1][3];
 
  drawPos[4][1] = pos[2][1];
  drawPos[4][2] = pos[2][2];
  drawPos[4][3] = pos[2][3];
  
  strokeWeight(lineD);
  stroke(Color[1] ,Color[2] , Color[3]);
            
  line(drawPos[1][1] , drawPos[1][2] , drawPos[1][3] 
     , drawPos[2][1] , drawPos[2][2] , drawPos[2][3]);
     
     stroke(Color[1] * 0.6f ,Color[2] * 0.6f , Color[3] * 0.6f);
     
  line(drawPos[2][1] , drawPos[2][2] , drawPos[2][3] 
     , drawPos[3][1] , drawPos[3][2] , drawPos[3][3]);
     
     stroke(Color[1] * 0.2f ,Color[2] * 0.2f , Color[3] * 0.2f);
     
  line(drawPos[3][1] , drawPos[3][2] , drawPos[3][3] 
     , drawPos[4][1] , drawPos[4][2] , drawPos[4][3]);
}
  

  public void update(){
  
  
  float xb = abshypot(pos[2][1] - pos[1][1] , pos[2][3] - pos[1][3]);
  float L1 = xb - limb0;
  float L2 = hypot(L1 , pos[2][2] - pos[1][2]);
//float K1 = cosine(limb1 , L2 , limb2);
  float K2 = cosine(limb2 , L2 , limb1);
  float K3 = cos(L1/L2);
  float K4 = K2 + K3;
  float L3 = sin(K4) * limb2;
  float L4 = cos(K4) * limb2;
  //float K5 = sin(time);
  float K5 = atan(pos[2][3] / pos[2][1] );
  float L5 = xb - L4;
  
  drawPos[1][1] = pos[1][1];
  drawPos[1][2] = pos[1][2];
  drawPos[1][3] = pos[1][3];
      
  drawPos[2][1] = (cos(K5) * limb0) + pos[1][1];
  drawPos[2][2] = pos[1][2];
  drawPos[2][3] = (sin(K5) * limb0) + pos[1][3];
  
  drawPos[3][1] = (cos(K5) * L5) + pos[1][1];
  drawPos[3][2] = L3;
  drawPos[3][3] = (sin(K5) * L5) + pos[1][3];
 
  drawPos[4][1] = pos[2][1];
  drawPos[4][2] = pos[2][2];
  drawPos[4][3] = pos[2][3];
  
  strokeWeight(lineD);
  stroke(Color[1] ,Color[2] , Color[3]);
            
  line(drawPos[1][1] , drawPos[1][2] , drawPos[1][3] 
     , drawPos[2][1] , drawPos[2][2] , drawPos[2][3]);
     
     stroke(Color[1] * 0.6f ,Color[2] * 0.6f , Color[3] * 0.6f);
     
  line(drawPos[2][1] , drawPos[2][2] , drawPos[2][3] 
     , drawPos[3][1] , drawPos[3][2] , drawPos[3][3]);
     
     stroke(Color[1] * 0.2f ,Color[2] * 0.2f , Color[3] * 0.2f);
     
  line(drawPos[3][1] , drawPos[3][2] , drawPos[3][3] 
     , drawPos[4][1] , drawPos[4][2] , drawPos[4][3]);
}
} 



/*
class HLine { 
  float ypos, speed; 
  HLine (float y, float s) {  
    ypos = y; 
    speed = s; 
  } 
  void update() { 
    ypos += speed; 
    if (ypos > height) { 
      ypos = 0; 
    } 
    line(0, ypos, width, ypos); 
  } 
} 
*/
public float hypot(float x , float y){
  return sqrt((x*x)+(y*y));
}

public float abshypot(float x , float y){
  return sqrt(abs((x*x)+(y*y)));
}
public float cosine(float a , float b , float c){
  float abase = ((a*a)+(b*b)-(c*c));
  float bbase = 2*a*b;
  return acos(abase / bbase);
}
/**
cylinder taken from http://wiki.processing.org/index.php/Cylinder
@author matt ditton
@modified by Abbas Noureddine, to draw a cone with specified width, dimeter of both
top and bottom. (if top == bottom, then you have a cylinder)
plus added a translation to draw the cone at the center of the bottom side
*/
 
public void cylinder(float bottom, float top, float h, int sides, float Ax, float Ay , float Az, PVector location)
{
  pushMatrix();
  translate(location.x , location.y- h/2 , location.z);
  
  rotateX(Ax);
  rotateY(Ay);
  rotateZ(Az);
  
  
  
  translate(0,h/2,0);
  
  float angle;
  float[] x = new float[sides+1];
  float[] z = new float[sides+1];
  
  float[] x2 = new float[sides+1];
  float[] z2 = new float[sides+1];
 
  //get the x and z position on a circle for all the sides
  for(int i=0; i < x.length; i++){
    angle = TWO_PI / (sides) * i;
    x[i] = sin(angle) * bottom;
    z[i] = cos(angle) * bottom;
  }
  
  for(int i=0; i < x.length; i++){
    angle = TWO_PI / (sides) * i;
    x2[i] = sin(angle) * top;
    z2[i] = cos(angle) * top;
  }
 
  //draw the bottom of the cylinder
  beginShape(TRIANGLE_FAN);
 
  vertex(0,   -h/2,    0);
 
  for(int i=0; i < x.length; i++){
    vertex(x[i], -h/2, z[i]);
  }
 
  endShape();
 
  //draw the center of the cylinder
  beginShape(QUAD_STRIP); 
 
  for(int i=0; i < x.length; i++){
    vertex(x[i], -h/2, z[i]);
    vertex(x2[i], h/2, z2[i]);
  }
 
  endShape();
 
  //draw the top of the cylinder
  beginShape(TRIANGLE_FAN); 
 
  vertex(0,   h/2,    0);
 
  for(int i=0; i < x.length; i++){
    vertex(x2[i], h/2, z2[i]);
  }
 
  endShape();
  
  popMatrix();
}




class Vec3 extends PVector {
  Vec3() { super(); }
  Vec3(float x, float y) { super(x, y); }
  Vec3(float x, float y, float z) { super(x, y, z); }
  Vec3(PVector v) { super(); set(v); }

  public String toString() {
    return String.format("< %+.2f, %+.2f, %+.2f >",
      x, y, z);
  }

  public PVector rotate(float angle) {
    return rotateZ(angle);
  }

  public PVector rotateX(float angle) {
    float cosa = cos(angle);
    float sina = sin(angle);
    float tempy = y;
    y = cosa * y - sina * z;
    z = cosa * z + sina * tempy;
    return this;
  }

  public PVector rotateY(float angle) {
    float cosa = cos(angle);
    float sina = sin(angle);
    float tempz = z;
    z = cosa * z - sina * x;
    x = cosa * x + sina * tempz;
    return this;
  }

  public PVector rotateZ(float angle) {
    float cosa = cos(angle);
    float sina = sin(angle);
    float tempx = x;
    x = cosa * x - sina * y;
    y = cosa * y + sina * tempx;
    return this;
  }
}

Overlord mech1 = new Overlord(100);
class Overlord{
  
Leg Leg1 = new Leg(20 , 150 , 150 , 255 , 105 , 180 , 10);
Leg Leg2 = new Leg(20 , 150 , 150 , 255 , 0 , 0 , 10);
Leg Leg3 = new Leg(20 , 150 , 150 , 0 , 255 , 0 , 10);
Leg Leg4 = new Leg(20 , 150 , 150 , 0 , 0 , 255 , 10);

  float radius;
  float[][] bPoint = new float[3][4];
  float[][][] bPointG = new float[3][5][4];
  
  Overlord(float Radius){
    radius = Radius;
  }
  
  public void setPoint(float x,float y, float z){
    bPoint[1][1] = x;
    bPoint[1][2] = y;
    bPoint[1][3] = z;
  }
  
  public void setRotation(float x,float y, float z){
    bPoint[2][1] = x;
    bPoint[2][2] = y;
    bPoint[2][3] = z;
  }
  
  public void setEndPoint1(float x,float y, float z){
    bPointG[2][1][1] = x;
    bPointG[2][1][2] = y;
    bPointG[2][1][3] = z;
  }
  
  public void setEndPoint2(float x,float y, float z){
    bPointG[2][2][1] = x;
    bPointG[2][2][2] = y;
    bPointG[2][2][3] = z;
  }
  
  public void setEndPoint3(float x,float y, float z){
    bPointG[2][3][1] = x;
    bPointG[2][3][2] = y;
    bPointG[2][3][3] = z;
  }
  
  public void setEndPoint4(float x,float y, float z){
    bPointG[2][4][1] = x;
    bPointG[2][4][2] = y;
    bPointG[2][4][3] = z;
  }
  
  
  public void makeSmtNice(){
    
  }
  
  public void update(){

     
     Vec3 v0, v1, v2, v3, cylinder;


     
     
    
    bPointG[1][1][1] = radius / sqrt(2) ;
    bPointG[1][1][2] = 0;
    bPointG[1][1][3] = radius / sqrt(2);
    
    bPointG[1][2][1] = -radius / sqrt(2);
    bPointG[1][2][2] = 0;
    bPointG[1][2][3] = radius / sqrt(2);
    
    bPointG[1][3][1] = -radius / sqrt(2);
    bPointG[1][3][2] = 0;
    bPointG[1][3][3] = -radius / sqrt(2);
    
    bPointG[1][4][1] = radius / sqrt(2);
    bPointG[1][4][2] = 0;
    bPointG[1][4][3] = -radius / sqrt(2);
    
  v0 = new Vec3(bPointG[1][1][1], bPointG[1][1][2], bPointG[1][1][3]);
  v1 = new Vec3(bPointG[1][2][1], bPointG[1][2][2], bPointG[1][2][3]);
  v2 = new Vec3(bPointG[1][3][1], bPointG[1][3][2], bPointG[1][3][3]);
  v3 = new Vec3(bPointG[1][4][1], bPointG[1][4][2], bPointG[1][4][3]);
  
  cylinder = new Vec3(bPoint[1][1] , bPoint[1][2] , bPoint[1][3]);
  
  v0.rotateX(bPoint[2][1]);
  v1.rotateX(bPoint[2][1]);
  v2.rotateX(bPoint[2][1]);
  v3.rotateX(bPoint[2][1]);
  
  v0.rotateY(bPoint[2][2]);
  v1.rotateY(bPoint[2][2]);
  v2.rotateY(bPoint[2][2]);
  v3.rotateY(bPoint[2][2]);
  
  v0.rotateZ(bPoint[2][3]);
  v1.rotateZ(bPoint[2][3]);
  v2.rotateZ(bPoint[2][3]);
  v3.rotateZ(bPoint[2][3]);
  
  
    
  
    
  Leg1.setBeginningPoint(v0.x  + bPoint[1][1] , v0.y  + bPoint[1][2] , v0.z  + bPoint[1][3] );
  Leg2.setBeginningPoint(v1.x  + bPoint[1][1] , v1.y  + bPoint[1][2] , v1.z  + bPoint[1][3] );
  Leg3.setBeginningPoint(v2.x  + bPoint[1][1] , v2.y  + bPoint[1][2] , v2.z  + bPoint[1][3] );
  Leg4.setBeginningPoint(v3.x  + bPoint[1][1] , v3.y  + bPoint[1][2] , v3.z  + bPoint[1][3] );
  
  Leg1.setEndgPoint(bPointG[2][1][1] , bPointG[2][1][2] , bPointG[2][1][3]);
  Leg2.setEndgPoint(bPointG[2][2][1] , bPointG[2][2][2] , bPointG[2][2][3]);
  Leg3.setEndgPoint(bPointG[2][3][1] , bPointG[2][3][2] , bPointG[2][3][3]);
  Leg4.setEndgPoint(bPointG[2][4][1] , bPointG[2][4][2] , bPointG[2][4][3]);
    
    Leg1.update();
    Leg2.update(-1);
    Leg3.update(-1);
    Leg4.update();
    
    
     stroke(0);
     fill(100);
     
    cylinder(radius , radius , 10 , 20 , bPoint[2][1] , bPoint[2][2] , bPoint[2][3] , cylinder);
  }
}



public float getExtremum(float point1 , float point2){
    float place = 0;

  if ((point1 > 0) && (point2 > 0)) {
    place = 0;
  }
    else if((point1 < 0) && (point2 > 0)) {
    place = 1;
  }
  else if ((point1 < 0) && (point2 < 0)) {
    place = 2;
  }
  else if ((point1 > 0) && (point2 < 0)) {
    place = 3;
  }
  
  point1 = abs(point1);
  point2 = abs(point2);
  return (90.0f * point2) / (point1 * point2) + (place * 90.0f);
}



public float getMissingPoint(){
  
  return 0;
}
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "FuckThisShitImOut_Mk1" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
