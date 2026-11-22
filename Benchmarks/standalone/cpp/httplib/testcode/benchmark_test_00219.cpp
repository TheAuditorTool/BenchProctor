// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unordered_map>

namespace httplib {
struct Request {
    std::string get_param_value(const std::string &key) const;
    std::string get_header_value(const std::string &key) const;
    std::unordered_map<std::string, std::string> path_params;
    std::string body;
};
struct Response {
    void set_content(const std::string &s, const std::string &type);
    void set_header(const std::string &key, const std::string &val);
    void set_redirect(const std::string &url, int status);
    int status;
};
struct Result {};
struct Client {
    Client(const std::string &host, int port);
    Result Post(const std::string &path, const std::string &body, const std::string &content_type);
};
}
extern "C" int RAND_bytes(unsigned char *buf, int num);
struct Payload { std::string value; };

void benchmark_test_00219(const httplib::Request &, httplib::Response &res)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    unsigned char _rnd[16];
    if (RAND_bytes(_rnd, sizeof(_rnd)) != 1) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    char _hex[33];
    for (int _i = 0; _i < 16; ++_i) std::snprintf(_hex + 2 * _i, 3, "%02x", _rnd[_i]);
    std::cout << "token for " << data << ": " << _hex << std::endl;
    res.set_content("ok", "text/plain");
}
