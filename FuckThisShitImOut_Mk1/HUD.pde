void HUD(float x ,float y ,float z , float Ax ,float Ay ,float Az){
    cam.beginHUD();
      strokeWeight(1);
   stroke(128);
  fill(0, 128);
  rect(0, 0, 70, 30);
  
  rect(0, 30, 110, 720);
  fill(255);
  text("" + nfc(frameRate, 2), 10, 18);
  text(" xAngle - " + round(x * 57.2958), 10, 41);
  text(" yAngle - " + round(y * 57.2958), 10, 52);
  text(" zAngle - " + round(z * 57.2958), 10, 63);
  
  text(" xDistance - " + round(Ax), 10, 74);
  text(" yDistance - " + round(Ay), 10, 85);
  text(" zDistance - " + round(Az), 10, 96);
  int i = 96;
  int a = 1;
  
  i = i + 15;
  text(" Leg 1 - " , 10 , i);
  i = i + 11;
  text(" Point 1 - " + round(mech1.Leg1.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg1.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg1.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 2 - " + round(mech1.Leg1.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg1.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg1.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 3 - " + round(mech1.Leg1.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg1.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg1.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 4 - " + round(mech1.Leg1.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg1.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg1.drawPos[a][3]), 10, i);
  
  a = 1;
  
  
  
  
  
  
  i = i + 15;
  text(" Leg 2 - " , 10 , i);
  i = i + 11;
  text(" Point 1 - " + round(mech1.Leg2.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg2.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg2.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 2 - " + round(mech1.Leg2.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg2.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg2.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 3 - " + round(mech1.Leg2.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg2.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg2.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 4 - " + round(mech1.Leg2.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg2.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg2.drawPos[a][3]), 10, i);
  
  a = 1;
  
  
  
  
  
  
  
  i = i + 15;
  text(" Leg 3 - " , 10 , i);
  i = i + 11;
  text(" Point 1 - " + round(mech1.Leg3.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg3.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg3.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 2 - " + round(mech1.Leg3.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg3.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg3.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 3 - " + round(mech1.Leg3.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg3.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg3.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 4 - " + round(mech1.Leg3.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg3.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg3.drawPos[a][3]), 10, i);
  
  a = 1;
  
  
  
  
  
  
  i = i + 15;
  text(" Leg 4 - " , 10 , i);
  i = i + 11;
  text(" Point 1 - " + round(mech1.Leg4.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg4.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg4.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 2 - " + round(mech1.Leg4.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg4.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg4.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 3 - " + round(mech1.Leg4.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg4.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg4.drawPos[a][3]), 10, i);
  
  a++;
  
  i = i + 13;
  text(" Point 4 - " + round(mech1.Leg4.drawPos[a][1]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg4.drawPos[a][2]), 10, i);
  i = i + 11;
  text("            - " + round(mech1.Leg4.drawPos[a][3]), 10, i);
  
  a = 1;
  
  cam.endHUD();
}