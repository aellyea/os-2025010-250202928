#include <iostream>
using namespace std;

int main() {
    long long i = 0;
    cout << "Program uji resource berjalan...\n";

    while (true) {
        for (long long j = 0; j < 100000000; j++) {}

        i++;
        cout << "Iterasi ke-" << i << endl;
    }
    return 0;
}

