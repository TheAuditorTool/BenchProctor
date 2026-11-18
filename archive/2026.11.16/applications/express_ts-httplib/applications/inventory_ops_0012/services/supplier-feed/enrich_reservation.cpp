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

void enrich_reservation(const httplib::Request &, httplib::Response &res)
{
    const char *phrase_env = std::getenv("DB_ROW_VALUE");
    std::string phrase = phrase_env ? std::string(phrase_env) : std::string();
    std::string backorder;
    if (!phrase.empty()) backorder = phrase;
    std::string restock;
    for (char _c : backorder) {
        if (_c == '&') restock += "&amp;";
        else if (_c == '<') restock += "&lt;";
        else if (_c == '>') restock += "&gt;";
        else if (_c == '"') restock += "&quot;";
        else if (_c == '\'') restock += "&#39;";
        else restock.push_back(_c);
    }
    res.set_content(std::string("<div class=\"comment\" data-author=\"") + restock + "\">" + restock + "</div>", "text/html");
}
