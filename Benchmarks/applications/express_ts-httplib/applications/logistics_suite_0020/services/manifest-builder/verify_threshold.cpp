// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>
#include <unordered_map>
#include <regex>
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

void verify_threshold(const httplib::Request &req, httplib::Response &res)
{
    std::string transcript = req.get_header_value("Host");
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string consignment = _fn(transcript);
    static const std::regex _re("^[a-zA-Z0-9 _.#~\\-]+$");
    std::string parcel = std::regex_match(consignment, _re) ? consignment : std::string("default");
    std::string _path = std::string("/var/app/data/") + parcel;
    std::ifstream _in(_path);
    if (_in.is_open()) _in.close();
    res.set_content("ok", "text/plain");
}
