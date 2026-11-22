// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
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

void export_record(const httplib::Request &, httplib::Response &res)
{
    const char *wording_env = std::getenv("USER_COMMENT");
    std::string wording = wording_env ? std::string(wording_env) : std::string();
    std::string handshake;
    if (!wording.empty()) handshake = wording;
    std::string subject = std::regex_match(handshake, std::regex("^(config|data|index|schema)$")) ? handshake : std::string("config");
    std::string _path = std::string("/var/app/data/") + subject;
    std::ifstream _in(_path);
    if (_in.is_open()) _in.close();
    res.set_content("ok", "text/plain");
}
