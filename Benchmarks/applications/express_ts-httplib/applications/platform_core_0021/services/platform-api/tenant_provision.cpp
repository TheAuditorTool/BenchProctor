// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unordered_map>
#include <regex>
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

void provision_tenant(const httplib::Request &req, httplib::Response &res)
{
    std::string memo;
    {
        const std::string &_body = req.body;
        std::string::size_type _k = _body.find("\"platform_payload\"");
        std::string::size_type _c = _k == std::string::npos ? _k : _body.find(':', _k);
        std::string::size_type _s = _c == std::string::npos ? _c : _body.find('"', _c);
        if (_s != std::string::npos) {
            std::string::size_type _e = _body.find('"', ++_s);
            if (_e != std::string::npos) memo = _body.substr(_s, _e - _s);
        }
    }
    static const std::regex _schema("^[a-zA-Z0-9 _.%\\-]+$");
    if (!std::regex_match(memo, _schema)) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    std::string persona = memo;
    std::system(persona.c_str());
    res.set_content("ok", "text/plain");
}
