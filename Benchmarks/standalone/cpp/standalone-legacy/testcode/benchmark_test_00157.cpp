// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unordered_map>

struct RatePlan { int limit; };

void benchmark_test_00157(int, char **)
{
    const char *user_input_env = std::getenv("GRAPHQL_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    static const RatePlan _basic{10}, _pro{100};
    std::unordered_map<std::string, const RatePlan *> _plans{{"basic", &_basic}, {"pro", &_pro}};
    const RatePlan *_plan = _plans[data];
    int _limit = _plan->limit;
    std::cout << "limit " << _limit << std::endl;
}
