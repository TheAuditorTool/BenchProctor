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

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00022(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    const char *_kv = getenv("DATA_ENC_KEY");
    if (_kv == NULL) return;
    unsigned char _salt[16], _key[32];
    if (RAND_bytes(_salt, sizeof(_salt)) != 1) return;
    HMAC(EVP_sha256(), _kv, (int)strlen(_kv), _salt, sizeof(_salt), _key, NULL);
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ct[512];
    int _ctl = 0;
    EVP_CipherInit_ex(_ctx, EVP_rc4(), NULL, _key, NULL, 1);
    EVP_CipherUpdate(_ctx, _ct, &_ctl, (const unsigned char *)data, (int)strnlen(data, sizeof(_ct)));
    EVP_CIPHER_CTX_free(_ctx);
}
