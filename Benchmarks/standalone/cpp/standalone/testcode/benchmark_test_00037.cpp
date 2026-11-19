// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <unistd.h>
#include <sys/socket.h>
#include <netdb.h>
#include <regex>
#include <netinet/in.h>
#include <arpa/inet.h>

void benchmark_test_00037(int, char **)
{
    const char *user_input_env = std::getenv("MULTIPART_FIELD");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    std::string _authority = data;
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
    if (std::regex_search(std::string(_resolved), _pr)) return;
    std::string safe = data;
    struct addrinfo _hints;
    std::memset(&_hints, 0, sizeof(_hints));
    _hints.ai_family = AF_UNSPEC;
    _hints.ai_socktype = SOCK_STREAM;
    struct addrinfo *_res = nullptr;
    if (getaddrinfo(safe.c_str(), "80", &_hints, &_res) == 0 && _res) {
        int _sock = socket(_res->ai_family, _res->ai_socktype, _res->ai_protocol);
        if (_sock >= 0) { connect(_sock, _res->ai_addr, _res->ai_addrlen); close(_sock); }
        freeaddrinfo(_res);
    }
}
