// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/evp.h>

void benchmark_test_00419(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    char data[512];
    size_t _len = strlen(user_input);
    size_t _w = 0;
    while (_w < _len && _w < sizeof(data) - 1) { data[_w] = user_input[_w]; ++_w; }
    data[_w] = '\0';
    EVP_MD_CTX *_mdctx = EVP_MD_CTX_new();
    unsigned char _digest[64];
    unsigned int _dlen = 0;
    EVP_DigestInit_ex(_mdctx, EVP_sha256(), NULL);
    EVP_DigestUpdate(_mdctx, data, strlen(data));
    EVP_DigestFinal_ex(_mdctx, _digest, &_dlen);
    EVP_MD_CTX_free(_mdctx);
}
