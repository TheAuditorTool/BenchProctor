// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00212(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char data[512];
    size_t _len = strlen(user_input);
    size_t _w = 0;
    while (_w < _len && _w < sizeof(data) - 1) { data[_w] = user_input[_w]; ++_w; }
    data[_w] = '\0';
    char _path[512];
    snprintf(_path, sizeof(_path), "/var/app/data/%s", data);
    FILE *_f = fopen(_path, "r");
    if (_f) fclose(_f);
}
