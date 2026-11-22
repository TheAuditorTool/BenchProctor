// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/evp.h>

void benchmark_test_00040(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    char data[512];
    size_t _len = strlen(user_input);
    size_t _w = 0;
    while (_w < _len && _w < sizeof(data) - 1) { data[_w] = user_input[_w]; ++_w; }
    data[_w] = '\0';
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
