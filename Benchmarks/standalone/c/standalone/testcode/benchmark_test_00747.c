// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <fcntl.h>

struct c_payload { const char *value; };

void benchmark_test_00747(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    unsigned char _rnd[16];
    int _fd = open("/dev/urandom", O_RDONLY);
    if (_fd >= 0) { if (read(_fd, _rnd, sizeof(_rnd)) < 0) _rnd[0] = 0; close(_fd); }
    printf("token for %s: %02x\n", data, _rnd[0]);
}
