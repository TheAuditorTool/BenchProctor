// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/sha.h>

void benchmark_test_01035(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    unsigned char _digest[32];
    SHA256((const unsigned char *)user_input, strlen(user_input), _digest);
}
