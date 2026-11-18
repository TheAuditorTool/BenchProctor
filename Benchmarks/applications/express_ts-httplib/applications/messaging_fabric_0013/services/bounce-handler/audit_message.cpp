// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
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

void audit_message(const httplib::Request &req, httplib::Response &res)
{
    std::string summary = req.get_header_value("Referer");
    std::string bulletin = !summary.empty() ? summary : std::string();
    std::string snippet;
    for (char _c : bulletin) {
        if (_c == '&') snippet += "&amp;";
        else if (_c == '<') snippet += "&lt;";
        else if (_c == '>') snippet += "&gt;";
        else if (_c == '"') snippet += "&quot;";
        else if (_c == '\'') snippet += "&#39;";
        else snippet.push_back(_c);
    }
    res.set_content(std::string("<div class=\"comment\" data-author=\"") + snippet + "\">" + snippet + "</div>", "text/html");
}
