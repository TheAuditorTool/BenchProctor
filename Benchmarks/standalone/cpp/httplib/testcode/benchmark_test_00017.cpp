// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
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
extern "C" int RAND_priv_bytes(unsigned char *buf, int num);

void benchmark_test_00017(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.body;
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    unsigned char _rnd[16];
    if (RAND_priv_bytes(_rnd, sizeof(_rnd)) != 1) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    char _hex[33];
    for (int _i = 0; _i < 16; ++_i) std::snprintf(_hex + 2 * _i, 3, "%02x", _rnd[_i]);
    std::cout << "token for " << data << ": " << _hex << std::endl;
    res.set_content("ok", "text/plain");
}
