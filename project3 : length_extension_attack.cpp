#include <iostream>
#include <string>
#include"sm3.h"
using namespace std;

int main() {
	string m = "64646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464";
	string result = iteration(m);  //SM3(m)，无填充的hash值
	cout << "扩展攻击前：" << result << endl;
	string extend = "61616161616161616161616161616161"; //扩展128bit消息
	string extensionB = "", compressB = "";
	extensionB = extension(HexToBin(extend));
	//将原hash值与扩展消息进行compress
	compressB = compress(extensionB, result);
	result = XOR(result, compressB);
	cout << "扩展攻击后：" << result;
}

