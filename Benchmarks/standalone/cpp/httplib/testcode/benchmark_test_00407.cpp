// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
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

void benchmark_test_00407(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_param_value("field");
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::srand((unsigned)std::time(nullptr));
    int _token = std::rand();
    std::cout << "token for " << data << ": " << _token << std::endl;
    res.set_content("ok", "text/plain");
}
