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

void benchmark_test_00455(const httplib::Request &, httplib::Response &res)
{
    const char *user_input_env = std::getenv("USER_COMMENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::string safe;
    for (char _c : data) {
        if (_c == '&') safe += "&amp;";
        else if (_c == '<') safe += "&lt;";
        else if (_c == '>') safe += "&gt;";
        else if (_c == '"') safe += "&quot;";
        else if (_c == '\'') safe += "&#39;";
        else safe.push_back(_c);
    }
    res.set_content(std::string("<div class=\"comment\" data-author=\"") + safe + "\">" + safe + "</div>", "text/html");
}
