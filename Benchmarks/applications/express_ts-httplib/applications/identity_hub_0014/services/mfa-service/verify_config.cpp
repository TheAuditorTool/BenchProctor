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

void verify_config(const httplib::Request &, httplib::Response &res)
{
    const char *snippet_env = std::getenv("USER_COMMENT");
    std::string snippet = snippet_env ? std::string(snippet_env) : std::string();
    std::string persona;
    if (!snippet.empty()) persona = snippet;
    res.set_content(std::string("<div class=\"comment\" data-author=\"") + persona + "\">" + persona + "</div>", "text/html");
}
