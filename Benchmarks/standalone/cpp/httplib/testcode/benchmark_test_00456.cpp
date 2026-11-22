// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
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

void benchmark_test_00456(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("Host");
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    const size_t _rec_size = 64;
    long _count = std::strtol(data.c_str(), nullptr, 10);
    if (_count <= 0 || _count > 65536) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    size_t _bytes = (size_t)_count * _rec_size;
    char *_recs = new (std::nothrow) char[_bytes];
    delete[] _recs;
    res.set_content("ok", "text/plain");
}
