// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <fstream>

void benchmark_test_00200(int, char **)
{
    const char *user_input_env = std::getenv("UPLOAD_NAME");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _path = std::string("/var/app/data/") + user_input;
    std::ifstream _in(_path);
    if (_in.is_open()) _in.close();
}
