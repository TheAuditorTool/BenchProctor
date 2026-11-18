#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00255() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00255 "$@"
