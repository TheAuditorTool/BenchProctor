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

void benchmark_test_00886(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("Cookie");
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    const long _unit_cents = 1999;
    long _qty = std::strtol(data.c_str(), nullptr, 10);
    if (_qty < 0 || _qty > 100000) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    long _total = _qty * _unit_cents;
    std::cout << "total=" << _total << std::endl;
    res.set_content("ok", "text/plain");
}
