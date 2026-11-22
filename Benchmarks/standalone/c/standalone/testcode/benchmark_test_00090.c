// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <fcntl.h>

void benchmark_test_00090(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    unsigned char _rnd[16];
    int _fd = open("/dev/urandom", O_RDONLY);
    if (_fd < 0) return;
    ssize_t _got = read(_fd, _rnd, sizeof(_rnd));
    close(_fd);
    if (_got != (ssize_t)sizeof(_rnd)) return;
    char _hex[33];
    for (int _i = 0; _i < 16; _i++) snprintf(_hex + 2 * _i, 3, "%02x", _rnd[_i]);
    printf("token for %s: %s\n", user_input, _hex);
}
