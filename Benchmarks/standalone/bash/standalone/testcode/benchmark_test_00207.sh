#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00207() {
  user_input="$HTTP_AUTHORIZATION"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  _host=$(echo "$data" | sed -E "s#^[a-zA-Z]+://##; s#[/:].*##")
  case "$_host" in "["*|"") echo "private range blocked"; exit 1;; esac
  _ip=$(getent ahosts "$_host" 2>/dev/null | head -n1 | cut -d" " -f1)
  _ip="${_ip:-$_host}"
  if ! echo "$_ip" | grep -qE "^[0-9]{1,3}(\.[0-9]{1,3}){3}$"; then echo "non-ipv4 host blocked" >&2; exit 1; fi
  if echo "$_ip" | grep -qE "^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)"; then echo "private range blocked"; exit 1; fi
  target_url="$data"
  _rest="${target_url#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00207 "$@"
