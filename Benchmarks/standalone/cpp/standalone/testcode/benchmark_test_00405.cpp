// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

struct pg_conn; typedef struct pg_conn PGconn;
struct pg_result; typedef struct pg_result PGresult;
extern "C" PGconn *PQsetdbLogin(const char *, const char *, const char *, const char *, const char *, const char *, const char *);
extern "C" int PQstatus(const PGconn *);
extern "C" void PQfinish(PGconn *);
extern "C" PGresult *PQexec(PGconn *, const char *);
extern "C" PGresult *PQexecParams(PGconn *, const char *, int, const unsigned int *, const char *const *, const int *, const int *, int);
extern "C" void PQclear(PGresult *);
static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00405(int, char **)
{
    const char *user_input_env = std::getenv("APP_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = cpp_own(user_input);
    std::string safe = std::regex_match(data, std::regex("^(asc|desc|name|created)$")) ? data : std::string("asc");
    PGconn *_pgc = PQsetdbLogin("db.internal", "5432", nullptr, nullptr, "appdb", "app", "");
    std::string _pgq = std::string("SELECT * FROM users WHERE name = '") + safe + "'";
    PGresult *_pgr = PQexec(_pgc, _pgq.c_str());
    PQclear(_pgr);
    PQfinish(_pgc);
}
