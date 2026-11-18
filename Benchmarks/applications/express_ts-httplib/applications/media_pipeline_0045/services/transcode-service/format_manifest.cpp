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

void format_manifest(const httplib::Request &req, httplib::Response &res)
{
    std::string notice = req.get_header_value("Referer");
    std::string rendition = !notice.empty() ? notice : std::string();
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
