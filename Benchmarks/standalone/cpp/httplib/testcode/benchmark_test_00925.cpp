// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>
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

void benchmark_test_00925(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("User-Agent");
    char _dst[16];
    size_t _n = user_input.size();
    std::memcpy(_dst, user_input.c_str(), _n + 1);
    std::cout << _dst << std::endl;
    res.set_content("ok", "text/plain");
}
