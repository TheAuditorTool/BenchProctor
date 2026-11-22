// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <ctime>
#include <random>
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

void benchmark_test_00086(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("Referer");
    Payload _pd{user_input};
    std::string data = _pd.value;
    std::mt19937 _gen(static_cast<std::mt19937::result_type>(std::time(nullptr)));
    std::uniform_int_distribution<int> _dist(0, 999999);
    int _token = _dist(_gen);
    std::cout << "token for " << data << ": " << _token << std::endl;
    res.set_content("ok", "text/plain");
}
