// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00240(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    char data[512];
    size_t _li = 0;
    for (; user_input[_li] != '\0' && _li < sizeof(data) - 1; ++_li) data[_li] = user_input[_li];
    data[_li] = '\0';
    char *_parts[2];
    _parts[0] = malloc(strlen(data) + 1);
    if (_parts[0] == NULL) return;
    strcpy(_parts[0], data);
    _parts[1] = NULL;
    printf("%s\n", _parts[0]);
    for (int _k = 0; _k < 2; _k++) free(_parts[_k]);
}
