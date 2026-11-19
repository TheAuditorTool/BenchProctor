// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <regex>

struct sqlite3; struct sqlite3_stmt;
extern "C" int sqlite3_open(const char *, sqlite3 **);
extern "C" int sqlite3_exec(sqlite3 *, const char *, int (*)(void *, int, char **, char **), void *, char **);
extern "C" int sqlite3_prepare_v2(sqlite3 *, const char *, int, sqlite3_stmt **, const char **);
extern "C" int sqlite3_bind_text(sqlite3_stmt *, int, const char *, int, void (*)(void *));
extern "C" int sqlite3_step(sqlite3_stmt *);
extern "C" int sqlite3_finalize(sqlite3_stmt *);
static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00299(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data = cpp_own(user_input);
    static const std::regex _re("^[a-zA-Z0-9_.#\\-]+$");
    std::string safe = std::regex_match(data, _re) ? data : std::string("default");
    sqlite3 *_db = nullptr;
    sqlite3_open("app.db", &_db);
    std::string _sqlq = std::string("SELECT * FROM users WHERE name = '") + safe + "'";
    sqlite3_exec(_db, _sqlq.c_str(), nullptr, nullptr, nullptr);
}
