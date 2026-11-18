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

void publish_checkpoint(const httplib::Request &req, httplib::Response &res)
{
    std::string note = req.get_header_value("Cookie");
    std::string addendum;
    for (std::string::size_type _i = 0; _i < note.size(); ++_i) {
        if (note[_i] == '%' && _i + 2 < note.size()) {
            addendum.push_back((char)std::strtol(note.substr(_i + 1, 2).c_str(), nullptr, 16));
            _i += 2;
        } else { addendum.push_back(note[_i]); }
    }
    std::string _cmd = std::string("ls ") + addendum;
    std::system(_cmd.c_str());
    res.set_content("ok", "text/plain");
}
