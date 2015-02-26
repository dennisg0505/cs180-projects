#include <iostream>

using namespace std;

bool twoSum(int a[], int n, int z);

int main() {
	int input[] = {0, 1, 2, 3, 5, 7, 9};
	cout << twoSum(input, 7, 9) << endl;
}

bool twoSum(int a[], int n, int z) {
	int i = 0;
	int j = n-1;
	int sum;
	while (i < j) {
		sum = a[i] + a[j];
		if (sum > z) {
			j--;
		} else if (sum < z) {
			i++;
		} else {
			return true;
		}
	}
	return false;
}