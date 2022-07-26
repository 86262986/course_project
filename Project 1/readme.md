# **项目**简介
## 项目名称
Implement the naïve birthday attack of reduced SM3
## 项目文件名


# 代码说明  
1、逐次计算sm3(m)的值re，准备找到前20bit的碰撞
```C++
string n = DecToBin(i); //int i to binary string m

string m = BinToHex(n);

string paddingValue = padding(m);

string result = iteration(paddingValue); //SM3(m) value

string re = HexToBin(result);
```
2、找到前20bit的碰撞：
在每次计算之后，根据re的前20bit，在字典中查找是否有相同的前20bit的碰撞。
如果找到碰撞则成功，否则将i(原像m的十进制数字表示)和re前20bit存放入字典中，继续寻找碰撞。
```C++
map<string, int>::iterator iter = hashMap.find(re.substr(0, j));

if (hashMap.end() == iter) {

hashMap[re.substr(0, j)] = i;

}

else {

QueryPerformanceCounter(&nEndTime);//停止计时

cout << " Preimage of the first 20-bit collision: " << iter->second << " and " << i << endl;

break;

}
```

# 运行指导
实验环境：Visual Studio 2022
注：添加头文件Project1-3: SM3.h时，文件名需改成sm3.h
运行结果：打印前20bit碰撞的原像，及所用时间
# 代码运行全过程截图
![[Pasted image 20220726153157.png]]

# 参考文献
无