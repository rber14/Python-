/*
*  @Roberto Campos
*  @Phys163
*  @Jan 31 2018
*
*
*   Write a C++ program that calculates the position, velocity, and acceleration of a particle moving along a line as follows:
*   x(t)=3.4(0.15t)-0.9t 2(0.26t).
*   Do this for 0t50 using functions for x, v, and a. Specify a reasonably small t, much less than one, when finding v and a.
*   The function x should have one parameter (t), while the functions for v and a should also receive the t used for the derivative calculations. These functions should call the x(t) function! You must use user-defined functions to receive credit.
*   Have the program output t, x, v, and a to a file and use matplotlib to plot the results on a single set of axes.
*/

#include <iostream>
#include <cstdlib>
#include <math.h>
#include <fstream>
#include <iomanip>

using std::cout;
using std::cin;
using std::endl;
using std::setw;

double func(double t)
{
   double pos;
   
   pos = 3.4*cos(.15*t)-0.9*(sqrt(t))*pow(sin(.26*t), 2); 
   return pos;
}

double veloc(double t, double dt)
{
   double vel;
   
   vel = (func((t+dt))-func(t))/dt;
   return vel;
}

double acc(double t, double dt)
{
   double accel;
   
   accel = (func(t+dt)+func(t-dt)-2*func(t))/pow(dt,2);
   return accel;
}



int main(int argc, char** argv)
{
   
   double pos;
   double vel;
   double accel;
   double delT = .01;
   int count=1;
   
   double t=0;
   std::ofstream myfile("theHwProj1.dat");
   if(myfile.is_open())
   {
      while(t<50)
      {
         pos = func(t);
         vel = veloc(t,delT);
         accel = acc(t,delT);
         myfile << t << std::right << setw(20) << pos << std::right << setw(22) << vel << std::right << setw(20) << accel << endl;
         t+=.01;
      }
      myfile.close();
      cout << "Successful" << endl;
   }
   else cout << "Unable to open file" << endl;
     
   return EXIT_SUCCESS;
}
