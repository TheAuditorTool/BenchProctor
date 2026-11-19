// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <unistd.h>
#include <unordered_map>

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

void benchmark_test_00116(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("Referer");
    std::string data;
    if (!user_input.empty()) data = user_input;
    std::string _path = std::string("/var/app/data/") + data;
    if (FILE *_f = std::fopen(_path.c_str(), "r")) std::fclose(_f);
    res.set_content("ok", "text/plain");
}
