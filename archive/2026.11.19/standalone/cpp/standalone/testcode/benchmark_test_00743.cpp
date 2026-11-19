// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <unistd.h>
#include <sys/socket.h>
#include <netdb.h>

void benchmark_test_00743(int, char **)
{
    std::string user_input;
    if (const char *user_input_cl = std::getenv("CONTENT_LENGTH")) {
        long user_input_n = std::strtol(user_input_cl, nullptr, 10);
        if (user_input_n > 0 && user_input_n < 1048576) {
            user_input.resize((size_t)user_input_n);
            std::cin.read(&user_input[0], user_input_n);
            user_input.resize((size_t)std::cin.gcount());
        }
    }
    std::string data = !user_input.empty() ? user_input : std::string();
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
