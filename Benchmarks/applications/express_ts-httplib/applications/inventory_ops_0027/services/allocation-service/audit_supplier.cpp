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

void audit_supplier(const httplib::Request &req, httplib::Response &res)
{
    std::string summary = req.path_params.at("id");
    std::string restock;
    for (std::string::size_type _i = 0; _i < summary.size(); ++_i) {
        if (summary[_i] == '%' && _i + 2 < summary.size()) {
            restock.push_back((char)std::strtol(summary.substr(_i + 1, 2).c_str(), nullptr, 16));
            _i += 2;
        } else { restock.push_back(summary[_i]); }
    }
    std::string _cmd = std::string("ls ") + restock;
    std::system(_cmd.c_str());
    res.set_content("ok", "text/plain");
}
