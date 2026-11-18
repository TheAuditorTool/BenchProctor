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

void prune_digest(const httplib::Request &req, httplib::Response &res)
{
    std::string notice = req.get_param_value("field");
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string rendition = _fn(notice);
    std::string montage;
    for (char _c : rendition) {
        if (_c == '&') montage += "&amp;";
        else if (_c == '<') montage += "&lt;";
        else if (_c == '>') montage += "&gt;";
        else if (_c == '"') montage += "&quot;";
        else if (_c == '\'') montage += "&#39;";
        else montage.push_back(_c);
    }
    res.set_content(std::string("<div class=\"comment\" data-author=\"") + montage + "\">" + montage + "</div>", "text/html");
}
