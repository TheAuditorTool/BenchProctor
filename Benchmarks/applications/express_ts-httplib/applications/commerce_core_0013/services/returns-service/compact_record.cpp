// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
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

void compact_record(const httplib::Request &, httplib::Response &res)
{
    const char *wording_env = std::getenv("ORDERS_INPUT_0013");
    std::string wording = wording_env ? std::string(wording_env) : std::string();
    std::string backorder;
    std::string::size_type _w = 0;
    while (_w < wording.size()) { backorder.push_back(wording[_w]); ++_w; }
    std::string _path = std::string("/var/app/data/") + backorder;
    if (FILE *_f = std::fopen(_path.c_str(), "w")) std::fclose(_f);
    res.set_content("ok", "text/plain");
}
