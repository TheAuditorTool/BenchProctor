// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unordered_map>

namespace httplib {
struct Request {
    std::string get_param_value(const std::string &key) const;
    std::string get_header_value(const std::string &key) const;
    std::unordered_map<std::string, std::string> path_params;
    std::string body;
};
struct Response {
    void set_content(const std::string &s, const std::string &type);
    void set_header(const std::string &key, const std::string &val);
    void set_redirect(const std::string &url, int status);
    int status;
};
struct Result {};
struct Client {
    Client(const std::string &host, int port);
    Result Post(const std::string &path, const std::string &body, const std::string &content_type);
};
}
struct env_md_st; typedef struct env_md_st EVP_MD;
typedef struct evp_md_ctx_st EVP_MD_CTX;
extern "C" EVP_MD_CTX *EVP_MD_CTX_new(void);
extern "C" void EVP_MD_CTX_free(EVP_MD_CTX *);
extern "C" const EVP_MD *EVP_md4(void);
extern "C" const EVP_MD *EVP_sha256(void);
extern "C" int EVP_DigestInit_ex(EVP_MD_CTX *, const EVP_MD *, void *);
extern "C" int EVP_DigestUpdate(EVP_MD_CTX *, const void *, size_t);
extern "C" int EVP_DigestFinal_ex(EVP_MD_CTX *, unsigned char *, unsigned int *);

void benchmark_test_00189(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("User-Agent");
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    EVP_MD_CTX *_mdctx = EVP_MD_CTX_new();
    unsigned char _digest[64];
    unsigned int _dlen = 0;
    EVP_DigestInit_ex(_mdctx, EVP_md4(), nullptr);
    EVP_DigestUpdate(_mdctx, data.data(), data.size());
    EVP_DigestFinal_ex(_mdctx, _digest, &_dlen);
    EVP_MD_CTX_free(_mdctx);
    std::cout << "digest " << (int)_digest[0] << std::endl;
    res.set_content("ok", "text/plain");
}
