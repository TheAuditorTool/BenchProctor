// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include <unordered_map>
#include <cctype>
#include <climits>

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

void validate_profile(const httplib::Request &, httplib::Response &res)
{
    const char *footnote_env = std::getenv("USER_COMMENT");
    std::string footnote = footnote_env ? std::string(footnote_env) : std::string();
    std::string consignment;
    switch (footnote.empty() ? '\0' : footnote[0]) {
        case '\0':
            consignment.clear();
            break;
        default:
            consignment = footnote;
            break;
    }
    std::string _joined = std::string("/var/app/data/") + consignment;
    char _resolved[PATH_MAX];
    if (!realpath(_joined.c_str(), _resolved)) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    if (std::string(_resolved).rfind("/var/app/data/", 0) != 0) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    std::string parcel = _resolved;
    if (FILE *_f = std::fopen(parcel.c_str(), "w")) std::fclose(_f);
    res.set_content("ok", "text/plain");
}
