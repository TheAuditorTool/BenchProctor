// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>
#include <unistd.h>
#include <unordered_map>
#include <regex>
#include <sys/socket.h>
#include <netdb.h>
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

void pull_supplier_feed(const httplib::Request &req, httplib::Response &res)
{
    std::string memo;
    {
        const std::string &_body = req.body;
        std::string::size_type _k = _body.find("\"inventory_payload\"");
        std::string::size_type _c = _k == std::string::npos ? _k : _body.find(':', _k);
        std::string::size_type _s = _c == std::string::npos ? _c : _body.find('"', _c);
        if (_s != std::string::npos) {
            std::string::size_type _e = _body.find('"', ++_s);
            if (_e != std::string::npos) memo = _body.substr(_s, _e - _s);
        }
    }
    std::string _authority = memo;
    std::string::size_type _scheme = _authority.find("://");
    if (_scheme != std::string::npos) _authority = _authority.substr(_scheme + 3);
    else if (_authority.rfind("//", 0) == 0) _authority = _authority.substr(2);
    _authority = _authority.substr(0, _authority.find_first_of("/?#"));
    std::string::size_type _userinfo = _authority.rfind('@');
    if (_userinfo != std::string::npos) _authority = _authority.substr(_userinfo + 1);
    _authority = _authority.substr(0, _authority.find(':'));
    static const std::regex _hw("^(api\\.internal\\.example\\.com|cdn\\.internal\\.example\\.com)$");
    if (!std::regex_match(_authority, _hw)) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    std::string backorder = memo;
    struct addrinfo _hints;
    std::memset(&_hints, 0, sizeof(_hints));
    _hints.ai_family = AF_UNSPEC;
    _hints.ai_socktype = SOCK_STREAM;
    struct addrinfo *_res = nullptr;
    if (getaddrinfo(backorder.c_str(), "80", &_hints, &_res) == 0 && _res) {
        int _sock = socket(_res->ai_family, _res->ai_socktype, _res->ai_protocol);
        if (_sock >= 0) { connect(_sock, _res->ai_addr, _res->ai_addrlen); close(_sock); }
        freeaddrinfo(_res);
    }
    res.set_content("ok", "text/plain");
}
