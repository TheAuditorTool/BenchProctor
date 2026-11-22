// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
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

void audit_batch(const httplib::Request &req, httplib::Response &res)
{
    std::string wording = req.get_header_value("X-Custom-Header");
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", wording.c_str());
    std::string addendum = _fmt_buf;
    std::string _page = "<section class=\"profile\" title=\"{{name}}\"><h2>{{name}}</h2></section>";
    std::string::size_type _at = 0;
    while ((_at = _page.find("{{name}}", _at)) != std::string::npos) {
        _page.replace(_at, 8, addendum);
        _at += addendum.size();
    }
    res.set_content(_page, "text/html");
}
