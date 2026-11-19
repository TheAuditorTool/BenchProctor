// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00796(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data = cpp_own(user_input);
    struct { int id; int flags; } _rec = { 0, 0 };
    _rec.id = std::atoi(data.c_str());
    std::cout << _rec.id << " " << _rec.flags << std::endl;
}
