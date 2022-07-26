#include <iostream>
#include <string>
#include <map>
#include<windows.h> 
#include"sm3.h"
using namespace std;

int main() {
	int i = 0;
	int j = 20;
	map<string, int> hashMap;

	double time = 0;
	LARGE_INTEGER nFreq;
	LARGE_INTEGER nBeginTime;
	LARGE_INTEGER nEndTime;
	QueryPerformanceFrequency(&nFreq);
	QueryPerformanceCounter(&nBeginTime);//开始计时  

	while (1) {
		string n = DecToBin(i); //int i to binary string m
		string m = BinToHex(n);
		string paddingValue = padding(m);
		string result = iteration(paddingValue); //SM3(m) value
		string re = HexToBin(result);

		//try to find collision
		map<string, int>::iterator iter = hashMap.find(re.substr(0, j));
		if (hashMap.end() == iter) {
			hashMap[re.substr(0, j)] = i;
		}
		else {
			QueryPerformanceCounter(&nEndTime);//停止计时  
			cout << " Preimage of the first 20-bit collision: " << iter->second << " and " << i << endl;
			break;
		}
		i++;
	}
	time = (double)(nEndTime.QuadPart - nBeginTime.QuadPart) / (double)nFreq.QuadPart;  
	cout << "Time：" << time << "s" << endl;



}

