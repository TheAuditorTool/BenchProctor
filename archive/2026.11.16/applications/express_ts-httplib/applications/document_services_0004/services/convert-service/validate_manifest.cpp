// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
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
struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void validate_manifest(const httplib::Request &, httplib::Response &res)
{
    const char *excerpt_env = std::getenv("USER_COMMENT");
    std::string excerpt = excerpt_env ? std::string(excerpt_env) : std::string();
    HeldValue _held(excerpt);
    const ValueSource &_vs = _held;
    std::string dossier = _vs.get();
    std::string addendum = std::regex_match(dossier, std::regex("^(config|data|index|schema)$")) ? dossier : std::string("config");
    std::string _path = std::string("/var/app/data/") + addendum;
    if (FILE *_f = std::fopen(_path.c_str(), "r")) std::fclose(_f);
    res.set_content("ok", "text/plain");
}
