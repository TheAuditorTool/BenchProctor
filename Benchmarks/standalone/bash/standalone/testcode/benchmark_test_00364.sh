#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00364() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  echo -n "$data" | sha256sum
}

benchmark_test_00364 "$@"
