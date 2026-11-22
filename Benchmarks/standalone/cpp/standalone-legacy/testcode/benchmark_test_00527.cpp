// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

typedef struct evp_cipher_st EVP_CIPHER;
typedef struct evp_cipher_ctx_st EVP_CIPHER_CTX;
extern "C" const EVP_CIPHER *EVP_des_ecb(void);
extern "C" const EVP_CIPHER *EVP_rc4(void);
extern "C" const EVP_CIPHER *EVP_aes_128_cbc(void);
extern "C" const EVP_CIPHER *EVP_aes_256_cbc(void);
extern "C" const EVP_CIPHER *EVP_aes_256_gcm(void);
extern "C" EVP_CIPHER_CTX *EVP_CIPHER_CTX_new(void);
extern "C" int EVP_EncryptInit_ex(EVP_CIPHER_CTX *, const EVP_CIPHER *, void *, const unsigned char *, const unsigned char *);
extern "C" int EVP_EncryptUpdate(EVP_CIPHER_CTX *, unsigned char *, int *, const unsigned char *, int);
extern "C" void EVP_CIPHER_CTX_free(EVP_CIPHER_CTX *);
extern "C" const EVP_CIPHER *EVP_aes_256_ecb(void);
extern "C" int EVP_EncryptInit_ex2(EVP_CIPHER_CTX *, const EVP_CIPHER *, const unsigned char *, const unsigned char *, const void *);

void benchmark_test_00527(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    const char *_kv = std::getenv("APP_ENC_KEY");
    unsigned char _ckey[32] = {0};
    if (_kv) std::strncpy(reinterpret_cast<char *>(_ckey), _kv, sizeof(_ckey) - 1);
    int _clen = data.size() > 512 ? 512 : static_cast<int>(data.size());
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    EVP_EncryptInit_ex2(_ctx, EVP_aes_256_ecb(), _ckey, nullptr, nullptr);
    unsigned char _cout[528]; int _coutl = 0;
    EVP_EncryptUpdate(_ctx, _cout, &_coutl, reinterpret_cast<const unsigned char *>(data.c_str()), _clen);
    EVP_CIPHER_CTX_free(_ctx);
}
