// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

struct sqlite3; struct sqlite3_stmt;
extern "C" int sqlite3_open(const char *, sqlite3 **);
extern "C" int sqlite3_exec(sqlite3 *, const char *, int (*)(void *, int, char **, char **), void *, char **);
extern "C" int sqlite3_prepare_v2(sqlite3 *, const char *, int, sqlite3_stmt **, const char **);
extern "C" int sqlite3_bind_text(sqlite3_stmt *, int, const char *, int, void (*)(void *));
extern "C" int sqlite3_step(sqlite3_stmt *);
extern "C" int sqlite3_finalize(sqlite3_stmt *);

void benchmark_test_00486(int, char **)
{
    const char *user_input_env = std::getenv("API_RESPONSE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _doc = std::string("{\"field\":\"") + user_input + "\"}";
    std::string::size_type _fs = _doc.find("\"field\":\"") + 9;
    std::string::size_type _fe = _doc.find('"', _fs);
    std::string data = _doc.substr(_fs, _fe - _fs);
    std::string safe = std::regex_match(data, std::regex("^(asc|desc|name|created)$")) ? data : std::string("asc");
    sqlite3 *_db = nullptr;
    sqlite3_open("app.db", &_db);
    std::string _sqlq = std::string("SELECT * FROM users WHERE name = '") + safe + "'";
    sqlite3_exec(_db, _sqlq.c_str(), nullptr, nullptr, nullptr);
}
