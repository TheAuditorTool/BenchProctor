// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unordered_map>

struct RatePlan { int limit; };

void benchmark_test_00406(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_FORWARDED_FOR");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    static const RatePlan _basic{10}, _pro{100};
    std::unordered_map<std::string, const RatePlan *> _plans{{"basic", &_basic}, {"pro", &_pro}};
    const RatePlan *_plan = _plans[data];
    int _limit = _plan ? _plan->limit : 0;
    std::cout << "limit " << _limit << std::endl;
}
