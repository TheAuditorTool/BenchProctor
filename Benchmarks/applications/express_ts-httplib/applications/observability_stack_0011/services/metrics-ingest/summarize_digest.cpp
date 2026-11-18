// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <unordered_map>
#include <cctype>
#include <climits>

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

void summarize_digest(const httplib::Request &req, httplib::Response &res)
{
    std::string caption = req.get_header_value("Referer");
    std::string _raw = caption;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string gauge = _closure();
    std::string _joined = std::string("/var/app/data/") + gauge;
    char _resolved[PATH_MAX];
    if (!realpath(_joined.c_str(), _resolved)) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    if (std::string(_resolved).rfind("/var/app/data/", 0) != 0) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    std::string cohort = _resolved;
    std::remove(cohort.c_str());
    res.set_content("ok", "text/plain");
}
