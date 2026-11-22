// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <unistd.h>
#include <sys/socket.h>
#include <netdb.h>

void benchmark_test_00146(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_ORIGIN");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    struct addrinfo _hints;
    std::memset(&_hints, 0, sizeof(_hints));
    _hints.ai_family = AF_UNSPEC;
    _hints.ai_socktype = SOCK_STREAM;
    struct addrinfo *_res = nullptr;
    if (getaddrinfo(data.c_str(), "80", &_hints, &_res) == 0 && _res) {
        int _sock = socket(_res->ai_family, _res->ai_socktype, _res->ai_protocol);
        if (_sock >= 0) { connect(_sock, _res->ai_addr, _res->ai_addrlen); close(_sock); }
        freeaddrinfo(_res);
    }
}
