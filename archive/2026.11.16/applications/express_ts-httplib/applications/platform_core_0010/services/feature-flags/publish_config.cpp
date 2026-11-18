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

void publish_config(const httplib::Request &, httplib::Response &res)
{
    const char *notice_env = std::getenv("PLATFORM_INPUT_0010");
    std::string notice = notice_env ? std::string(notice_env) : std::string();
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string persona = _fn(notice);
    static const std::regex _schema("^[a-zA-Z0-9 _.%\\-]+$");
    if (!std::regex_match(persona, _schema)) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    std::string handshake = persona;
    std::string _cmd = std::string("ls ") + handshake;
    std::system(_cmd.c_str());
    res.set_content("ok", "text/plain");
}
