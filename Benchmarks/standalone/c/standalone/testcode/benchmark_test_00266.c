// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <fcntl.h>

void benchmark_test_00266(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char data[512];
    size_t _len = strlen(user_input);
    size_t _w = 0;
    while (_w < _len && _w < sizeof(data) - 1) { data[_w] = user_input[_w]; ++_w; }
    data[_w] = '\0';
    char _resolved[1024];
    char _joined[1024];
    snprintf(_joined, sizeof(_joined), "/var/app/data/%s", data);
    if (realpath(_joined, _resolved) == NULL) return;
    if (strncmp(_resolved, "/var/app/data/", 14) != 0) return;
    const char *arg = _resolved;
    int _fd = open(arg, O_RDONLY);
    if (_fd >= 0) close(_fd);
}
