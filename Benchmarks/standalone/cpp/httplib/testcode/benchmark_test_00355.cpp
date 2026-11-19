// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include <climits>
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

void benchmark_test_00355(const httplib::Request &, httplib::Response &res)
{
    const char *user_input_env = std::getenv("APP_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::string _joined = std::string("/var/app/data/") + data;
    char _resolved[PATH_MAX];
    if (!realpath(_joined.c_str(), _resolved)) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    if (std::string(_resolved).rfind("/var/app/data/", 0) != 0) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    std::string safe = _resolved;
    if (FILE *_f = std::fopen(safe.c_str(), "w")) std::fclose(_f);
    res.set_content("ok", "text/plain");
}
