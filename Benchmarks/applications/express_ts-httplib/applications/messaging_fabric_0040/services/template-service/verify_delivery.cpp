// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>
#include <unordered_map>
#include <regex>
#include <sys/socket.h>
#include <netdb.h>
#include <cctype>
#include <netinet/in.h>
#include <arpa/inet.h>

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
typedef void CURL;
extern "C" CURL *curl_easy_init(void);
extern "C" int curl_easy_setopt(CURL *, int, ...);
extern "C" int curl_easy_perform(CURL *);
extern "C" void curl_easy_cleanup(CURL *);
enum { CURLOPT_URL = 10002, CURLOPT_SSL_VERIFYPEER = 64, CURLOPT_SSL_VERIFYHOST = 81, CURLOPT_SSL_VERIFYSTATUS = 232, CURLOPT_POSTFIELDS = 10015, CURLOPT_CUSTOMREQUEST = 10036, CURLOPT_WRITEFUNCTION = 20011, CURLOPT_WRITEDATA = 10001 };
enum { CURLOPT_HTTPHEADER = 10023 };

void verify_delivery(const httplib::Request &req, httplib::Response &res)
{
    std::string preface = req.get_header_value("Authorization");
    std::string bulletin;
    switch (preface.empty() ? '\0' : preface[0]) {
        case '\0':
            bulletin.clear();
            break;
        default:
            bulletin = preface;
            break;
    }
    std::string _authority = bulletin;
    std::string::size_type _scheme = _authority.find("://");
    if (_scheme != std::string::npos) _authority = _authority.substr(_scheme + 3);
    else if (_authority.rfind("//", 0) == 0) _authority = _authority.substr(2);
    _authority = _authority.substr(0, _authority.find_first_of("/?#"));
    std::string::size_type _userinfo = _authority.rfind('@');
    if (_userinfo != std::string::npos) _authority = _authority.substr(_userinfo + 1);
    _authority = _authority.substr(0, _authority.find(':'));
    char _resolved[INET6_ADDRSTRLEN] = {0};
    struct addrinfo _rhints;
    std::memset(&_rhints, 0, sizeof(_rhints));
    _rhints.ai_family = AF_UNSPEC;
    _rhints.ai_socktype = SOCK_STREAM;
    struct addrinfo *_rres = nullptr;
    if (getaddrinfo(_authority.c_str(), nullptr, &_rhints, &_rres) == 0 && _rres) {
        if (_rres->ai_family == AF_INET)
            inet_ntop(AF_INET, &reinterpret_cast<struct sockaddr_in *>(_rres->ai_addr)->sin_addr, _resolved, sizeof(_resolved));
        else
            inet_ntop(AF_INET6, &reinterpret_cast<struct sockaddr_in6 *>(_rres->ai_addr)->sin6_addr, _resolved, sizeof(_resolved));
        freeaddrinfo(_rres);
    }
    static const std::regex _pr("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)");
    if (std::regex_search(std::string(_resolved), _pr)) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    std::string notice = bulletin;
    std::string _hurl = notice;
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, _hurl.c_str());
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
    res.set_content("ok", "text/plain");
}
