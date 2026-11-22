// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

struct env_md_st; typedef struct env_md_st EVP_MD;
typedef struct evp_md_ctx_st EVP_MD_CTX;
extern "C" EVP_MD_CTX *EVP_MD_CTX_new(void);
extern "C" void EVP_MD_CTX_free(EVP_MD_CTX *);
extern "C" const EVP_MD *EVP_md4(void);
extern "C" const EVP_MD *EVP_sha256(void);
extern "C" int EVP_DigestInit_ex(EVP_MD_CTX *, const EVP_MD *, void *);
extern "C" int EVP_DigestUpdate(EVP_MD_CTX *, const void *, size_t);
extern "C" int EVP_DigestFinal_ex(EVP_MD_CTX *, unsigned char *, unsigned int *);

void benchmark_test_00508(int, char **)
{
    const char *user_input_env = std::getenv("APP_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    EVP_MD_CTX *_mdctx = EVP_MD_CTX_new();
    unsigned char _digest[64];
    unsigned int _dlen = 0;
    EVP_DigestInit_ex(_mdctx, EVP_md4(), nullptr);
    EVP_DigestUpdate(_mdctx, data.data(), data.size());
    EVP_DigestFinal_ex(_mdctx, _digest, &_dlen);
    EVP_MD_CTX_free(_mdctx);
    std::cout << "digest " << (int)_digest[0] << std::endl;
}
