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

void reconcile_profile(const httplib::Request &, httplib::Response &res)
{
    const char *excerpt_env = std::getenv("DB_ROW_VALUE");
    std::string excerpt = excerpt_env ? std::string(excerpt_env) : std::string();
    std::string dossier;
    if (!excerpt.empty()) dossier = excerpt;
    std::string addendum;
    for (char _c : dossier) {
        if (_c == '&') addendum += "&amp;";
        else if (_c == '<') addendum += "&lt;";
        else if (_c == '>') addendum += "&gt;";
        else if (_c == '"') addendum += "&quot;";
        else if (_c == '\'') addendum += "&#39;";
        else addendum.push_back(_c);
    }
    res.set_content(std::string("<div class=\"comment\" data-author=\"") + addendum + "\">" + addendum + "</div>", "text/html");
}
