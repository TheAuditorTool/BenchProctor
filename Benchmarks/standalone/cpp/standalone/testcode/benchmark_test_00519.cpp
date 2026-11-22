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
extern "C" int sqlite3_get_table(sqlite3 *, const char *, char ***, int *, int *, char **); extern "C" void sqlite3_free_table(char **);

void benchmark_test_00519(int, char **)
{
    const char *user_input_env = std::getenv("APP_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    static const std::regex _re("^[a-zA-Z0-9_.#\\-]+$");
    std::string arg = std::regex_match(data, _re) ? data : std::string("default");
    sqlite3 *_db = nullptr;
    sqlite3_open("app.db", &_db);
    std::string _sqlq = std::string("SELECT name, email FROM users WHERE name = '") + arg + "'";
    char **_rows = nullptr;
    int _nrow = 0, _ncol = 0;
    sqlite3_get_table(_db, _sqlq.c_str(), &_rows, &_nrow, &_ncol, nullptr);
    for (int _r = 1; _r <= _nrow; ++_r) std::cout << _rows[_r * _ncol + 1] << std::endl;
    sqlite3_free_table(_rows);
}
