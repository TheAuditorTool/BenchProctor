// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
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

void benchmark_test_00961(const httplib::Request &, httplib::Response &res)
{
    const char *user_input_env = std::getenv("USER_COMMENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    try { data = user_input; } catch (...) { data.clear(); }
    const int _rec_size = 64;
    int _count = std::atoi(data.c_str());
    int _bytes = _count * _rec_size;
    char *_recs = new (std::nothrow) char[(size_t)_bytes];
    delete[] _recs;
    res.set_content("ok", "text/plain");
}
