#include <iostream>
#include <string>
#include"sm3.h"
using namespace std;

int main() {
	string m = "64646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464646464";
	string result = iteration(m);  //SM3(m)��������hashֵ
	cout << "��չ����ǰ��" << result << endl;
	string extend = "61616161616161616161616161616161"; //��չ128bit��Ϣ
	string extensionB = "", compressB = "";
	extensionB = extension(HexToBin(extend));
	//��ԭhashֵ����չ��Ϣ����compress
	compressB = compress(extensionB, result);
	result = XOR(result, compressB);
	cout << "��չ������" << result;
}

