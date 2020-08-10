#include<stdio.h>
#include<stdlib.h>
#define gcx getchar_unlocked
typedef long int lint;


lint findMaxArr(lint arr[], int n){
    lint i, maxIdx = 0;
    for(i=0;i<n-1;i++){
        if(arr[i+1]>arr[i]){
            maxIdx = i+1;
        }
    }
    return maxIdx;
}

lint getValue(){
    lint n = 0;
    int c = gcx();
    while(c<'0' ||c>'9') c = gcx();
    while(c>='0' && c<='9'){
        n = n*10 + c-'0';
        c=gcx();
    }
    return n;
}
int main(){
    lint N = getValue();
    lint K = getValue();
    lint i,j,temp,maxIdx;
    
    lint *arrNum = (lint*)malloc(N * sizeof(lint));
    for(i=0;i<N;i++){
        arrNum[i] = getValue();
    }

    for(i=0;i<K;i++){
        maxIdx = findMaxArr(arrNum,N);
        arrNum[maxIdx] = arrNum[maxIdx]/2;
    }

    lint sum=0;
    for(i=0;i<N;i++){
        sum+=arrNum[i];
    }
    printf("%ld",sum);
}
