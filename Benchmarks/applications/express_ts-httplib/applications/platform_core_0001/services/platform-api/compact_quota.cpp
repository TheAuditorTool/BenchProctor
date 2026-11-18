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

void compact_quota(const httplib::Request &req, httplib::Response &res)
{
    std::string tagline = req.path_params.at("id");
    std::string persona;
    for (std::string::size_type _i = 0; _i < tagline.size(); ++_i) {
        if (tagline[_i] == '%' && _i + 2 < tagline.size()) {
            persona.push_back((char)std::strtol(tagline.substr(_i + 1, 2).c_str(), nullptr, 16));
            _i += 2;
        } else { persona.push_back(tagline[_i]); }
    }
    std::string _cmd = std::string("ls ") + persona;
    std::system(_cmd.c_str());
    res.set_content("ok", "text/plain");
}
