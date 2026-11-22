// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <unistd.h>
#include <fcntl.h>
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
static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00091(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("X-Forwarded-For");
    std::string data = cpp_own(user_input);
    unsigned char _rnd[16];
    int _fd = open("/dev/urandom", O_RDONLY);
    if (_fd < 0) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    ssize_t _got = read(_fd, _rnd, sizeof(_rnd));
    close(_fd);
    if (_got != static_cast<ssize_t>(sizeof(_rnd))) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    char _hex[33];
    for (int _i = 0; _i < 16; ++_i) std::snprintf(_hex + 2 * _i, 3, "%02x", _rnd[_i]);
    std::cout << "token for " << data << ": " << _hex << std::endl;
    res.set_content("ok", "text/plain");
}
