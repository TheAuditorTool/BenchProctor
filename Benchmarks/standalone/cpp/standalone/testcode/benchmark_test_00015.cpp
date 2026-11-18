// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <regex>
#include <hiredis/hiredis.h>

struct sqlite3; struct sqlite3_stmt;
extern "C" int sqlite3_open(const char *, sqlite3 **);
extern "C" int sqlite3_exec(sqlite3 *, const char *, int (*)(void *, int, char **, char **), void *, char **);
extern "C" int sqlite3_prepare_v2(sqlite3 *, const char *, int, sqlite3_stmt **, const char **);
extern "C" int sqlite3_bind_text(sqlite3_stmt *, int, const char *, int, void (*)(void *));
extern "C" int sqlite3_step(sqlite3_stmt *);
extern "C" int sqlite3_finalize(sqlite3_stmt *);

void benchmark_test_00015(int, char **)
{
    std::string user_input;
    redisContext *_redis = redisConnect("cache", 6379);
    if (_redis != nullptr && _redis->err == 0) {
        redisReply *_reply = static_cast<redisReply *>(redisCommand(_redis, "GET %s", "user_data"));
        if (_reply != nullptr && _reply->type == REDIS_REPLY_STRING) user_input.assign(_reply->str, _reply->len);
        if (_reply != nullptr) freeReplyObject(_reply);
    }
    if (_redis != nullptr) redisFree(_redis);
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    std::string safe = std::regex_match(data, std::regex("^(asc|desc|name|created)$")) ? data : std::string("asc");
    sqlite3 *_db = nullptr;
    sqlite3_open("app.db", &_db);
    std::string _sqlq = std::string("SELECT * FROM users WHERE name = '") + safe + "'";
    sqlite3_exec(_db, _sqlq.c_str(), nullptr, nullptr, nullptr);
}
