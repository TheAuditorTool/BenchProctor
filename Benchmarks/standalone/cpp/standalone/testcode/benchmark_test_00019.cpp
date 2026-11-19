// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <hiredis/hiredis.h>

typedef void CURL;
extern "C" CURL *curl_easy_init(void);
extern "C" int curl_easy_setopt(CURL *, int, ...);
extern "C" int curl_easy_perform(CURL *);
extern "C" void curl_easy_cleanup(CURL *);
enum { CURLOPT_URL = 10002, CURLOPT_SSL_VERIFYPEER = 64, CURLOPT_SSL_VERIFYHOST = 81, CURLOPT_SSL_VERIFYSTATUS = 232, CURLOPT_POSTFIELDS = 10015, CURLOPT_CUSTOMREQUEST = 10036, CURLOPT_WRITEFUNCTION = 20011, CURLOPT_WRITEDATA = 10001 };

void benchmark_test_00019(int, char **)
{
    std::string user_input;
    redisContext *_redis = redisConnect("cache", 6379);
    if (_redis != nullptr && _redis->err == 0) {
        redisReply *_reply = static_cast<redisReply *>(redisCommand(_redis, "GET %s", "user_data"));
        if (_reply != nullptr && _reply->type == REDIS_REPLY_STRING) user_input.assign(_reply->str, _reply->len);
        if (_reply != nullptr) freeReplyObject(_reply);
    }
    if (_redis != nullptr) redisFree(_redis);
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::string _hurl = data;
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, _hurl.c_str());
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
}
