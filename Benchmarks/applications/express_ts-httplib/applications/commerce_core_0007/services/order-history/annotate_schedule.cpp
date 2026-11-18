// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
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
static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void annotate_schedule(const httplib::Request &req, httplib::Response &res)
{
    std::string heading = req.get_header_value("User-Agent");
    std::string voucher = cpp_own(heading);
    std::string backorder = (voucher == "/bin/echo" || voucher == "/bin/cat") ? voucher : std::string("/bin/echo");
    std::system(backorder.c_str());
    res.set_content("ok", "text/plain");
}
