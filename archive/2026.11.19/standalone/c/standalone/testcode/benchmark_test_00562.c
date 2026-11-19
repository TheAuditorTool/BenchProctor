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

struct c_payload { const char *value; };

void benchmark_test_00562(int argc, char **argv)
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
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    unsigned char _iv[8];
    RAND_bytes(_iv, sizeof(_iv));
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ct[512];
    int _ctl = 0;
    EVP_EncryptInit_ex(_ctx, EVP_des_ede3_cbc(), NULL, (const unsigned char *)getenv("DATA_ENC_KEY"), _iv);
    EVP_EncryptUpdate(_ctx, _ct, &_ctl, (const unsigned char *)data, (int)strlen(data));
    EVP_CIPHER_CTX_free(_ctx);
}
