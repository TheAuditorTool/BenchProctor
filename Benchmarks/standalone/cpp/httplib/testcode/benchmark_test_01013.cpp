// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
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
extern "C" unsigned char *SHA256(const unsigned char *d, unsigned long n, unsigned char *md);
struct Payload { std::string value; };

void benchmark_test_01013(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("X-Custom-Header");
    Payload _pd{user_input};
    std::string data = _pd.value;
    unsigned char _digest[32];
    SHA256(reinterpret_cast<const unsigned char *>(data.c_str()), data.size(), _digest);
    std::cout << "digest " << (int)_digest[0] << std::endl;
    res.set_content("ok", "text/plain");
}
