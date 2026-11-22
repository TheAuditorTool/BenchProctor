// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>
#include <unordered_map>
#include <cctype>
#include <fstream>
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

void fetch_summary(const httplib::Request &req, httplib::Response &res)
{
    std::string transcript = req.get_param_value("field");
    std::string addendum;
    std::string::size_type _w = 0;
    while (_w < transcript.size()) { addendum.push_back(transcript[_w]); ++_w; }
    std::string _joined = std::string("/var/app/data/") + addendum;
    char _resolved[PATH_MAX];
    if (!realpath(_joined.c_str(), _resolved)) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    if (std::string(_resolved).rfind("/var/app/data/", 0) != 0) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    std::string byline = _resolved;
    std::ifstream _in(byline);
    if (_in.is_open()) _in.close();
    res.set_content("ok", "text/plain");
}
