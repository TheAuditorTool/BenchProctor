// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unordered_map>
#include <regex>
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

void build_header(const httplib::Request &req, httplib::Response &res)
{
    std::string summary = req.get_header_value("Authorization");
    std::string grievance;
    grievance.reserve(summary.size());
    for (char _c : summary) grievance.push_back(_c);
    std::string inquiry = std::regex_match(grievance, std::regex("^(plain|markdown|html|text)$")) ? grievance : std::string("plain");
    res.set_content(std::string("<div class=\"comment\" data-author=\"") + inquiry + "\">" + inquiry + "</div>", "text/html");
}
