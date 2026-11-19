// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>
#include <unistd.h>
#include <sys/socket.h>
#include <netdb.h>
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
struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void benchmark_test_01012(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_param_value("multipart_field");
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    struct addrinfo _hints;
    std::memset(&_hints, 0, sizeof(_hints));
    _hints.ai_family = AF_UNSPEC;
    _hints.ai_socktype = SOCK_STREAM;
    struct addrinfo *_res = nullptr;
    if (getaddrinfo(data.c_str(), "80", &_hints, &_res) == 0 && _res) {
        int _sock = socket(_res->ai_family, _res->ai_socktype, _res->ai_protocol);
        if (_sock >= 0) { connect(_sock, _res->ai_addr, _res->ai_addrlen); close(_sock); }
        freeaddrinfo(_res);
    }
    res.set_content("ok", "text/plain");
}
