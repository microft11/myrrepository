#include<iostream>
#include"studentlist.h"
using namespace std;
char ErrorMsg[][100]= {
	"",//0
	"查无此人",//1
	"被其他数据引用！不能删除！",//2
	"不在社团中！"//3
};
void showError(int idx) {
	cout<<ErrorMsg[idx]<<endl;
}

