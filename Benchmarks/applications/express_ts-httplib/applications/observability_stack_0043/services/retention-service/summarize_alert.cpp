// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unordered_map>
#include <cctype>
#include <hiredis/hiredis.h>

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
typedef void CURL;
extern "C" CURL *curl_easy_init(void);
extern "C" int curl_easy_setopt(CURL *, int, ...);
extern "C" int curl_easy_perform(CURL *);
extern "C" void curl_easy_cleanup(CURL *);
enum { CURLOPT_URL = 10002, CURLOPT_SSL_VERIFYPEER = 64, CURLOPT_SSL_VERIFYHOST = 81, CURLOPT_SSL_VERIFYSTATUS = 232, CURLOPT_POSTFIELDS = 10015, CURLOPT_CUSTOMREQUEST = 10036, CURLOPT_WRITEFUNCTION = 20011, CURLOPT_WRITEDATA = 10001 };
enum { CURLOPT_HTTPHEADER = 10023 };

void summarize_alert(const httplib::Request &, httplib::Response &res)
{
    std::string note;
    redisContext *_redis = redisConnect("cache", 6379);
    if (_redis != nullptr && _redis->err == 0) {
        redisReply *_reply = static_cast<redisReply *>(redisCommand(_redis, "GET %s", "user_data"));
        if (_reply != nullptr && _reply->type == REDIS_REPLY_STRING) note.assign(_reply->str, _reply->len);
        if (_reply != nullptr) freeReplyObject(_reply);
    }
    if (_redis != nullptr) redisFree(_redis);
    std::string gauge;
    switch (note.empty() ? '\0' : note[0]) {
        case '\0':
            gauge.clear();
            break;
        default:
            gauge = note;
            break;
    }
    std::string _hurl = gauge;
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, _hurl.c_str());
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
    res.set_content("ok", "text/plain");
}
