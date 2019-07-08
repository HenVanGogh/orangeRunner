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

void setBeginningPoint(float x , float y , float z){
  pos[1][1] = x;
  pos[1][2] = y;
  pos[1][3] = z;
}

void setEndgPoint(float x , float y , float z){
  pos[2][1] = x;
  pos[2][2] = y;
  pos[2][3] = z;
}

void update(float why){
  
  
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
     
     stroke(Color[1] * 0.6 ,Color[2] * 0.6 , Color[3] * 0.6);
     
  line(drawPos[2][1] , drawPos[2][2] , drawPos[2][3] 
     , drawPos[3][1] , drawPos[3][2] , drawPos[3][3]);
     
     stroke(Color[1] * 0.2 ,Color[2] * 0.2 , Color[3] * 0.2);
     
  line(drawPos[3][1] , drawPos[3][2] , drawPos[3][3] 
     , drawPos[4][1] , drawPos[4][2] , drawPos[4][3]);
}
  

  void update(){
  
  
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
     
     stroke(Color[1] * 0.6 ,Color[2] * 0.6 , Color[3] * 0.6);
     
  line(drawPos[2][1] , drawPos[2][2] , drawPos[2][3] 
     , drawPos[3][1] , drawPos[3][2] , drawPos[3][3]);
     
     stroke(Color[1] * 0.2 ,Color[2] * 0.2 , Color[3] * 0.2);
     
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
float hypot(float x , float y){
  return sqrt((x*x)+(y*y));
}

float abshypot(float x , float y){
  return sqrt(abs((x*x)+(y*y)));
}
float cosine(float a , float b , float c){
  float abase = ((a*a)+(b*b)-(c*c));
  float bbase = 2*a*b;
  return acos(abase / bbase);
}