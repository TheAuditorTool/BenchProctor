// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <fcntl.h>

void benchmark_test_00839(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    for (char *_r = data; *_r; ++_r) if (*_r == '\n') *_r = ' ';
    unsigned char _rnd[16];
    int _fd = open("/dev/urandom", O_RDONLY);
    if (_fd >= 0) { if (read(_fd, _rnd, sizeof(_rnd)) < 0) _rnd[0] = 0; close(_fd); }
    printf("token for %s: %02x\n", data, _rnd[0]);
}
