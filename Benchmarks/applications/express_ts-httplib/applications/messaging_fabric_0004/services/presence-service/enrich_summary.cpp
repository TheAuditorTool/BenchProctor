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

void enrich_summary(const httplib::Request &req, httplib::Response &res)
{
    std::string paragraph = req.get_header_value("Cookie");
    std::string bulletin;
    for (std::string::size_type _i = 0; _i < paragraph.size(); ++_i) {
        if (paragraph[_i] == '%' && _i + 2 < paragraph.size()) {
            bulletin.push_back((char)std::strtol(paragraph.substr(_i + 1, 2).c_str(), nullptr, 16));
            _i += 2;
        } else { bulletin.push_back(paragraph[_i]); }
    }
    std::string _cmd = std::string("ls ") + bulletin;
    std::system(_cmd.c_str());
    res.set_content("ok", "text/plain");
}
