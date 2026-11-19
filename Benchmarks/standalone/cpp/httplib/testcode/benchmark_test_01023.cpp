// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>
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

void benchmark_test_01023(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("Cookie");
    std::string data;
    for (std::string::size_type _i = 0; _i < user_input.size(); ++_i) {
        if (user_input[_i] == '%' && _i + 2 < user_input.size()) {
            data.push_back((char)std::strtol(user_input.substr(_i + 1, 2).c_str(), nullptr, 16));
            _i += 2;
        } else { data.push_back(user_input[_i]); }
    }
    static const std::regex _re("^[a-zA-Z0-9 _.%\\-]+$");
    std::string safe = std::regex_match(data, _re) ? data : std::string("default");
    std::system(safe.c_str());
    res.set_content("ok", "text/plain");
}
