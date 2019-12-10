/*
To compile (if have root installed in your system)
root -l Ques_six.C

if dy/dt=f(y,t)
then
y(t0+h)=y(t0)+integral(f(y(t0),t0))[from t0 to t0+h]
above can be approximated as 
y(t0+h)~y(t0)+f(y(t0),t0)*h
above is use repetedly to obtain the function at different values.
y(t0+(n+1)h)~y(t0+n*h)+f(y(t0+n*h),t0)*h
*/

void Ques_six()
{
	float n0=0,
t0=0,
h=0.1,
tf=10;
float n[100],t[100];
n[0]=10;
for (unsigned int i = 0; i <100; i += 1)
{
	   n[i+1]=n[i]-1.5*n[i]*h;
	   t[i]=i*h;
	   
	   cout<<t[i]<<"   "<<n[i]<<endl;
}

  TGraph* g1 = new TGraph(100,t,n);
  g1->SetMarkerStyle(20);
  g1->SetMarkerSize(0.8);
  g1->SetMarkerColor(2);
  g1->SetLineColor(1);
  g1->SetTitle("Radioactive Decay;Time(s) ;n(cm^{-3}) ; Z axis");
  g1->Draw("APL");
}
