/*
*  @Roberto Campos
*  @Phys163
*  @Jan 31 2018
*  @Workcite: online resources
*
*  Write a C++ program to solve the following differential equation:
*  dzds=s z0.83+2s2(3z)
*  Over the domain 0s3 given the initial condition z(0)=3.2. 
*  Output the resulting function z(s) to a file (both the independent and dependent variables.
*/

#include <iostream>
#include <cmath>
#include <fstream>
#include <iomanip>

using std::cout;
using std::cin;
using std::endl;

double df(double s, double z)     
{
   double x = (sqrt(s)*pow(z,0.83)+2*pow(s,2)*sin(3*z)); //ODE given
   return x;
}

                                                      
int main(int argc, char** argv)
{
                         
    double s = 0;
    double z0 = 3.2;                                  //initial condition
    double interval = 3;                              // s=0 interval =3 so 0< s < 3, s will kep stepping .01 until you get to 3, if you want 0<s<100 then just define s as 100
    double step = .01;                                //dt
    double z;                                         //define z to later use inside loop
    
    std::ofstream myfile("zoft.dat");
    if(myfile.is_open()) 
    {
       while(fabs(interval-s)>0.0000001)              
       {   
           z=z0+(step*df(s,z0));                      //calculate new z, which is z0+step*dz/ds   
                                                      //You can add this line to see s and new z0: cout<<s<<std::setw(16)<<z0 << endl;
           myfile << s <<std::setw(16)<< z0 << endl;  // this line inputs data into file, s is the first column and z0 is the second column 
           z0=z;                                      //pass this new z as z0 in the next iteration.
           s=s+step;                                  //calculate new s.
       }  
     myfile.close();
     cout << "Done" ;
    } else cout << "Unable to open file" ;  
          
 
    return EXIT_SUCCESS;
}