#include<iostream>
using namespace std;

template <class nun>
void multiplicar(nun a, nun b);
template <class base>
void cuadrado(base a);

int main(){
    float j,k,i;
    cin>> j;
    cin>>k;
    cin>> i;
    multiplicar(j,k);
    cuadrado(i);
    return 0;
}


template <class nun>
void multiplicar(nun a, nun b){
    cout<<a*b<<endl;
}
template <class base>
void cuadrado(base a){
    cout<< a*a;
}
