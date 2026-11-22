// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/evp.h>
#include <openssl/rand.h>
#include <openssl/hmac.h>

void benchmark_test_00128(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    const char *_kv = getenv("DATA_ENC_KEY");
    if (_kv == NULL) return;
    unsigned char _salt[16], _key[32];
    if (RAND_bytes(_salt, sizeof(_salt)) != 1) return;
    HMAC(EVP_sha256(), _kv, (int)strlen(_kv), _salt, sizeof(_salt), _key, NULL);
    unsigned char _nonce[12];
    RAND_bytes(_nonce, sizeof(_nonce));
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ct[512];
    int _ctl = 0;
    EVP_CipherInit_ex(_ctx, EVP_chacha20_poly1305(), NULL, _key, _nonce, 1);
    EVP_CipherUpdate(_ctx, _ct, &_ctl, (const unsigned char *)data, (int)strnlen(data, sizeof(_ct)));
    EVP_CIPHER_CTX_free(_ctx);
}
