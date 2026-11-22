// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unordered_map>

struct RatePlan { int limit; };

void benchmark_test_00197(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    switch (user_input.empty() ? '\0' : user_input[0]) {
        case '\0':
            data.clear();
            break;
        default:
            data = user_input;
            break;
    }
    static const RatePlan _basic{10}, _pro{100};
    std::unordered_map<std::string, const RatePlan *> _plans{{"basic", &_basic}, {"pro", &_pro}};
    const RatePlan *_plan = _plans[data];
    int _limit = _plan ? _plan->limit : 0;
    std::cout << "limit " << _limit << std::endl;
}
