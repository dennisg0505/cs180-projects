#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<vector<int> > threeSum(vector<int> &num);

int main() {
	vector<int> input;
	int inputArray[] = {-1, 0, 1, 2, -1, 4};
	int inputSize = 6;
	for (int i = 0; i < inputSize; i++) {
		input.push_back(inputArray[i]);
	}

	vector<vector<int> > output = threeSum(input);

	for (int i = 0; i < output.size(); i++) {
		cout << "(";
		for (int j = 0; j < 3; j++) {
			if (j != 2) {
				cout << output[i][j] << ",";
			} else {
				cout << output[i][j];
			}
		}
		cout << ")" << endl;
	}
}

vector<vector<int> > threeSum(vector<int> &num) {
	vector<vector<int> > result;

	sort(num.begin(), num.end());

	for (int i = 0; i < num.size(); i++) {
		int j = i + 1;
		int k = num.size() - 1;
		while (j < k) {
			int sum = num[i] + num[j] + num[k];
			if (sum > 0) {
				k--;
			} else if (sum < 0) {
				j++;
			} else {
				vector<int> temp;
				temp.push_back(num[i]);
				temp.push_back(num[j]);
				temp.push_back(num[k]);
				if (find(result.begin(), result.end(), temp) == result.end()) {
					result.push_back(temp);
				}
				j++;
			}
		}
	}

	return result;
}