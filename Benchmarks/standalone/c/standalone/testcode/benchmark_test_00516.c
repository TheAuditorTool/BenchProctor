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

void benchmark_test_00516(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    FILE *_src_fp = fopen("/etc/app/config", "r");
    if (_src_fp != NULL) {
        if (fgets(user_input_buf, sizeof(user_input_buf), _src_fp) == NULL) user_input_buf[0] = '\0';
        fclose(_src_fp);
    }
    const char *user_input = user_input_buf;
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
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
