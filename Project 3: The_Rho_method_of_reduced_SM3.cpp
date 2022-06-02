#include <iostream>
#include <string> 
#include"sm3.h"
using namespace std;

string f(string n) { //对二进制字符串n做sm3的hash，返回二进制字符串结果
	string m = BinToHex(n);
	string paddingValue = padding(m);
	string result = iteration(paddingValue);
	string re = HexToBin(result);
	return re;
}

int main() {
 
	int64_t i0 = 2, i1 = 2;
	string n0 = DecToBin(i0);
	string n1 = DecToBin(i1);
	int j = 20;

	while (1) {
		string re0 = n0;
		string re1 = f(n1);
		string m0 = f(re0);
		string m1 = f(re1);

		//try to find collision
		if (m0.substr(0, j) == m1.substr(0, j)) {
			cout << "Preimage of the first 20-bit collision: " << "re0:" << re0 << "and re1:" << re1 << endl;
			return 0;
		}
	}
	cout << "Time：" << time << "s" << endl;
}
