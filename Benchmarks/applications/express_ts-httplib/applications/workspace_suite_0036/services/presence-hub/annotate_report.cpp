// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
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

void annotate_report(const httplib::Request &req, httplib::Response &res)
{
    std::string remark = req.get_header_value("Authorization");
    std::string synopsis;
    if (!remark.empty()) synopsis = remark;
    static const std::regex _schema("^[a-zA-Z0-9 _.%\\-]+$");
    if (!std::regex_match(synopsis, _schema)) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    std::string quotation = synopsis;
    std::system(quotation.c_str());
    res.set_content("ok", "text/plain");
}
