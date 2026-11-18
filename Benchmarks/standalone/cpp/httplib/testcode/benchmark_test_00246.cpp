// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
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

void benchmark_test_00246(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("Referer");
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    std::string safe = std::regex_match(data, std::regex("^(plain|markdown|html|text)$")) ? data : std::string("plain");
    res.set_content(std::string("<div class=\"comment\" data-author=\"") + safe + "\">" + safe + "</div>", "text/html");
}
