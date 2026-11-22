#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00025() {
  user_input="$HTTP_X_FORWARDED_FOR"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  printf '%s' "$data" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 3 --symmetric --cipher-algo AES256 -o /var/app/run/record.gpg 3<<<"$DATA_ENC_KEY"
}

benchmark_test_00025 "$@"
