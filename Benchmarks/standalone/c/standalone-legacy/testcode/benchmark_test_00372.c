// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/evp.h>

void benchmark_test_00372(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    FILE *_src_fp = fopen("/tmp/data", "r");
    if (_src_fp != NULL) {
        if (fgets(user_input_buf, sizeof(user_input_buf), _src_fp) == NULL) user_input_buf[0] = '\0';
        fclose(_src_fp);
    }
    const char *user_input = user_input_buf;
    char data[512];
    size_t _li = 0;
    for (; user_input[_li] != '\0' && _li < sizeof(data) - 1; ++_li) data[_li] = user_input[_li];
    data[_li] = '\0';
    EVP_MD_CTX *_mdctx = EVP_MD_CTX_new();
    unsigned char _digest[64];
    unsigned int _dlen = 0;
    EVP_DigestInit_ex(_mdctx, EVP_md4(), NULL);
    EVP_DigestUpdate(_mdctx, data, strlen(data));
    EVP_DigestFinal_ex(_mdctx, _digest, &_dlen);
    EVP_MD_CTX_free(_mdctx);
}
