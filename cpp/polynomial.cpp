#include<iostream>
using namespace std;
#include<math.h>
float pow2(int x)
{

return x*x;

}

void usingForLoop()
{


int n;cin>>n;
cout<<pow2(3)<<sqrt(4)<<"\n";
float x[n];
float y[n];
int i=0;
while(i<=n-1)
{
cin>>x[i];
cin>>y[i];
i++;
}

float sum=0;
i=0;
while(i<n-1)
{

float dx = x[i]-x[i+1];
float dy = y[i]-y[i+1];

 sum+=float(sqrt(pow2(dx)+pow2(dy)));

i++;
}
float Dx = x[n-1] - x[0];
float Dy = y[n-1] -y[0];
float fd = pow2(Dx)+pow2(Dy);

sum=sum+float(sqrt(fd));
cout<<sum;


}

float usingWhileLoop(float x[],float y[],int n)
{
int i=0;
float sum=0;

while(i<n-1)
{

float dx = x[i]-x[i+1];
float dy = y[i]-y[i+1];

 sum+=float(sqrt(pow2(dx)+pow2(dy)));

i++;
}
float Dx = x[n-1] - x[0];
float Dy = y[n-1] -y[0];
float fd = pow2(Dx)+pow2(Dy);

sum=sum+float(sqrt(fd));
return sum;

}

float usingForLoop(float x[],float y[],int n)
{

int i=0;
float sum=0;
for(i=0;i<=n-1;i++)
{

float dx = x[i]-x[i+1];
float dy = y[i]-y[i+1];

 sum+=float(sqrt(pow2(dx)+pow2(dy)));

i++;
}
float Dx = x[n-1] - x[0];
float Dy = y[n-1] -y[0];
float fd = pow2(Dx)+pow2(Dy);

sum=sum+float(sqrt(fd));
return sum;

}



int main()
{

int n;cin>>n;

float x[n];
float y[n];
int i=0;
for(int i=0;i<=n;i++)
{
cin>>x[i];
cin>>y[i];
i++;
}
cout<<usingWhileLoop(x,y,n)<<"\n";
cout<<usingForLoop(x,y,n);


}

