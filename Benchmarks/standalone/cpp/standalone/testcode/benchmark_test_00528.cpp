// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <unordered_map>

struct RatePlan { int limit; };

void benchmark_test_00528(int, char **)
{
    std::string user_input;
    if (const char *user_input_cl = std::getenv("CONTENT_LENGTH")) {
        long user_input_n = std::strtol(user_input_cl, nullptr, 10);
        if (user_input_n > 0 && user_input_n < 1048576) {
            user_input.resize((size_t)user_input_n);
            std::cin.read(&user_input[0], user_input_n);
            user_input.resize((size_t)std::cin.gcount());
        }
    }
    std::string data;
    try { data = user_input; } catch (...) { data.clear(); }
    static const RatePlan _basic{10}, _pro{100};
    std::unordered_map<std::string, const RatePlan *> _plans{{"basic", &_basic}, {"pro", &_pro}};
    const RatePlan *_plan = _plans[data];
    int _limit = _plan ? _plan->limit : 0;
    std::cout << "limit " << _limit << std::endl;
}
