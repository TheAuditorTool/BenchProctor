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
static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00053(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.body;
    std::string data = cpp_own(user_input);
    char _dst[16];
    if (data.size() < sizeof(_dst)) std::strcpy(_dst, data.c_str());
    else _dst[0] = '\0';
    std::cout << _dst << std::endl;
    res.set_content("ok", "text/plain");
}
