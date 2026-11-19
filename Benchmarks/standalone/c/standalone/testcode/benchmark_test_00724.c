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

void benchmark_test_00724(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char data[512];
    switch (user_input[0]) {
        case '\0':
            data[0] = '\0';
            break;
        default:
            snprintf(data, sizeof(data), "%s", user_input);
            break;
    }
    const char *safe = data;
    if (strcmp(data, "api.internal.svc") != 0 && strcmp(data, "cdn.internal.svc") != 0) safe = "api.internal.svc";
    struct addrinfo _hints;
    struct addrinfo *_ai = NULL;
    memset(&_hints, 0, sizeof(_hints));
    _hints.ai_family = AF_UNSPEC;
    _hints.ai_socktype = SOCK_STREAM;
    if (getaddrinfo(safe, "80", &_hints, &_ai) == 0 && _ai) {
        int _sock = socket(_ai->ai_family, _ai->ai_socktype, _ai->ai_protocol);
        if (_sock >= 0) { connect(_sock, _ai->ai_addr, _ai->ai_addrlen); close(_sock); }
        freeaddrinfo(_ai);
    }
}
