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

void normalize_bundle(const httplib::Request &req, httplib::Response &res)
{
    std::string transcript = req.get_header_value("X-Custom-Header");
    std::string consignment;
    if (!transcript.empty()) consignment = transcript;
    std::string parcel = (consignment == "/bin/echo" || consignment == "/bin/cat") ? consignment : std::string("/bin/echo");
    std::system(parcel.c_str());
    res.set_content("ok", "text/plain");
}
