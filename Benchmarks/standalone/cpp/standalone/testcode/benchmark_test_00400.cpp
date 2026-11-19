// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>

struct Payload { std::string value; };

void benchmark_test_00400(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    int _x = 0;
    if (!data.empty()) _x = (int)data[0];
    std::cout << (_x + (int)data.size()) << std::endl;
}
