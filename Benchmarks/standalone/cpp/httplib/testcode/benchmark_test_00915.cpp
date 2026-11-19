// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <spawn.h>
#include <sys/wait.h>
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

void benchmark_test_00915(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("Cookie");
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    const char *_sp_argv[] = { "/usr/bin/grep", data.c_str(), nullptr };
    char *const _sp_env[] = { nullptr };
    pid_t _pid;
    if (posix_spawn(&_pid, "/usr/bin/grep", nullptr, nullptr, const_cast<char *const *>(_sp_argv), _sp_env) == 0) waitpid(_pid, nullptr, 0);
    res.set_content("ok", "text/plain");
}
