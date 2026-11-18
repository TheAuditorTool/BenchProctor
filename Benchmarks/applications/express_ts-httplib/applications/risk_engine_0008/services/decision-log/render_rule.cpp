// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unordered_map>
#include <cctype>

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

void render_rule(const httplib::Request &, httplib::Response &res)
{
    const char *synopsis_env = std::getenv("USER_COMMENT");
    std::string synopsis = synopsis_env ? std::string(synopsis_env) : std::string();
    std::string verdict = synopsis;
    for (char &_c : verdict) if (_c == '\n') _c = ' ';
    res.set_content(std::string("<div class=\"comment\" data-author=\"") + verdict + "\">" + verdict + "</div>", "text/html");
}
