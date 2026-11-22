#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00053() {
  user_input="$HTTP_REFERER"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  printf '%s' "$data" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 3 --symmetric --cipher-algo CAST5 --allow-old-cipher-algos -o /var/app/run/record.gpg 3<<<"$DATA_ENC_KEY"
}

benchmark_test_00053 "$@"
