// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/evp.h>

void benchmark_test_00568(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    EVP_MD_CTX *_mdctx = EVP_MD_CTX_new();
    unsigned char _digest[64];
    unsigned int _dlen = 0;
    EVP_DigestInit_ex(_mdctx, EVP_md4(), NULL);
    EVP_DigestUpdate(_mdctx, data, strlen(data));
    EVP_DigestFinal_ex(_mdctx, _digest, &_dlen);
    EVP_MD_CTX_free(_mdctx);
}
