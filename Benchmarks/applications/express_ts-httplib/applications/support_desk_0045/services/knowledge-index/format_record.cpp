// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>
#include <unordered_map>
#include <cctype>
#include <fstream>

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

void format_record(const httplib::Request &req, httplib::Response &res)
{
    std::string remark = req.get_header_value("Origin");
    std::string inquiry;
    switch (remark.empty() ? '\0' : remark[0]) {
        case '\0':
            inquiry.clear();
            break;
        default:
            inquiry = remark;
            break;
    }
    std::string _path = std::string("/var/app/data/") + inquiry;
    std::ifstream _in(_path);
    if (_in.is_open()) _in.close();
    res.set_content("ok", "text/plain");
}
