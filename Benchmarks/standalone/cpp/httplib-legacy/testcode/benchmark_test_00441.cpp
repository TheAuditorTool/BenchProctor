// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
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
    std::unordered_multimap<std::string, std::string> headers;
};
struct Result {};
struct Client {
    Client(const std::string &host, int port);
    Result Post(const std::string &path, const std::string &body, const std::string &content_type);
};
}

void benchmark_test_00441(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("User-Agent");
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    std::string _ckval = data;
    for (char &_c : _ckval) if (_c == '\r' || _c == '\n') _c = ' ';
    res.headers.emplace("Set-Cookie", std::string("session=") + _ckval + "; HttpOnly; SameSite=Strict; Path=/");
    res.set_content("ok", "text/plain");
}
