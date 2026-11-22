// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/evp.h>

void benchmark_test_00128(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    for (char *_r = data; *_r; ++_r) if (*_r == '\n') *_r = ' ';
    const char *_kv = getenv("DATA_ENC_KEY");
    if (_kv == NULL) return;
    unsigned char _key[32];
    EVP_Digest(_kv, strlen(_kv), _key, NULL, EVP_sha256(), NULL);
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ct[528];
    int _ctl = 0;
    EVP_EncryptInit_ex2(_ctx, EVP_aes_256_ecb(), _key, NULL, NULL);
    EVP_EncryptUpdate(_ctx, _ct, &_ctl, (const unsigned char *)data, (int)strnlen(data, 512));
    EVP_CIPHER_CTX_free(_ctx);
}
