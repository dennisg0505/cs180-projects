#include <iostream>

using namespace std;

int main() {
	int array[] = {0, 1, 2, 3, 4, 5, 7};

	int CELL = 0;

	for (int i = 1; i < 7; i++) {
		CELL = CELL ^ array[i];
	}

	for (int i = 0; i < 8; i++) {
		CELL = CELL ^ i;
	}

	cout << CELL << endl;
}