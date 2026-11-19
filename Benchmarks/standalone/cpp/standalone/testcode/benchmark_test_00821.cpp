// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

struct Payload { std::string value; };

void benchmark_test_00821(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    struct { int id; int flags; } _rec;
    _rec.id = std::atoi(data.c_str());
    std::cout << _rec.id << " " << _rec.flags << std::endl;
}
