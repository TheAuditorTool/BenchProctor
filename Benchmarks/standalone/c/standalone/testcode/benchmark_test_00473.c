// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <sys/socket.h>
#include <netdb.h>

void benchmark_test_00473(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    char data[512];
    size_t _li = 0;
    for (; user_input[_li] != '\0' && _li < sizeof(data) - 1; ++_li) data[_li] = user_input[_li];
    data[_li] = '\0';
    struct addrinfo _hints;
    struct addrinfo *_ai = NULL;
    memset(&_hints, 0, sizeof(_hints));
    _hints.ai_family = AF_UNSPEC;
    _hints.ai_socktype = SOCK_STREAM;
    if (getaddrinfo(data, "80", &_hints, &_ai) == 0 && _ai) {
        int _sock = socket(_ai->ai_family, _ai->ai_socktype, _ai->ai_protocol);
        if (_sock >= 0) { connect(_sock, _ai->ai_addr, _ai->ai_addrlen); close(_sock); }
        freeaddrinfo(_ai);
    }
}
