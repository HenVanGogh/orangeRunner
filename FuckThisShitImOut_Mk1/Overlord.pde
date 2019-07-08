
Overlord mech1 = new Overlord( 126.8095);
class Overlord{
  
Leg Leg1 = new Leg(56 , 202.240 , 173.215 , 255 , 105 , 180 , 10);
Leg Leg2 = new Leg(56 , 202.240 , 173.215 , 255 , 0 , 0 , 10);
Leg Leg3 = new Leg(56 , 202.240 , 173.215 , 0 , 255 , 0 , 10);
Leg Leg4 = new Leg(56 , 202.240 , 173.215 , 0 , 0 , 255 , 10);

  float radius;
  float[][] bPoint = new float[3][4];
  float[][][] bPointG = new float[3][5][4];
  

      
  
  Overlord(float Radius){
    radius = Radius;
  }
  
  void setPoint(float x,float y, float z){
    bPoint[1][1] = x;
    bPoint[1][2] = y;
    bPoint[1][3] = z;
  }
  
  void setRotation(float x,float y, float z){
    bPoint[2][1] = x;
    bPoint[2][2] = y;
    bPoint[2][3] = z;
  }
  
  void setEndPoint1(float x,float y, float z){
    bPointG[2][1][1] = x;
    bPointG[2][1][2] = y;
    bPointG[2][1][3] = z;
  }
  
  void setEndPoint2(float x,float y, float z){
    bPointG[2][2][1] = x;
    bPointG[2][2][2] = y;
    bPointG[2][2][3] = z;
  }
  
  void setEndPoint3(float x,float y, float z){
    bPointG[2][3][1] = x;
    bPointG[2][3][2] = y;
    bPointG[2][3][3] = z;
  }
  
  void setEndPoint4(float x,float y, float z){
    bPointG[2][4][1] = x;
    bPointG[2][4][2] = y;
    bPointG[2][4][3] = z;
  }
  
  
  void makeSmtNice(){
    
  }
  
  void update(){

     
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
    Leg4.update(); //<>//
    
    stroke(255,255,0);
    strokeWeight(30);
    
    PVector gravity = gravityRotation();
    point(gravity.x , gravity.y , gravity.z);
     stroke(90);
     fill(100);
     
    cylinder(radius , radius , 10 , 30 , bPoint[2][1] , bPoint[2][2] , bPoint[2][3] , cylinder);
  }
  
  
  
  PVector gravityRotation(){
    
    float sumX = 0 , sumZ = 0 , sumY = 0;
    
    for(int i = 0; i < 4 ; i = i + 1){
    sumX = sumX + Leg1.drawPos[i + 1][1];
    sumY = sumY + Leg1.drawPos[i + 1][2];
    sumZ = sumZ + Leg1.drawPos[i + 1][3];
   
    sumX = sumX + Leg2.drawPos[i + 1][1];
    sumY = sumY + Leg2.drawPos[i + 1][2];
    sumZ = sumZ + Leg2.drawPos[i + 1][3];
   
    sumX = sumX + Leg3.drawPos[i + 1][1];
    sumY = sumY + Leg3.drawPos[i + 1][2];
    sumZ = sumZ + Leg3.drawPos[i + 1][3];
    
    sumX = sumX + Leg4.drawPos[i + 1][1];
    sumY = sumY + Leg4.drawPos[i + 1][2];
    sumZ = sumZ + Leg4.drawPos[i + 1][3];
    }
    
    
    sumX = sumX / 16;
    sumY = sumY / 16;
    sumZ = sumZ / 16;
    
    return new PVector(sumX , sumY , sumZ);
  }
}



float getExtremum(float point1 , float point2){
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
  return (90.0 * point2) / (point1 * point2) + (place * 90.0);
}



float getMissingPoint(){
  
  return 0;
}

class Piece{
  PVector piece;
  
  Piece(){
  }
  void set(PVector a){
    piece = a;
  }
  
  PVector get(){
   return piece; 
  }
}
