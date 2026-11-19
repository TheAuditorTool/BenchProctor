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
struct Payload { std::string value; };

void benchmark_test_00450(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("Host");
    Payload _pd{user_input};
    std::string data = _pd.value;
    const char *_found = std::strchr(data.c_str(), '=');
    std::cout << *_found << std::endl;
    res.set_content("ok", "text/plain");
}
