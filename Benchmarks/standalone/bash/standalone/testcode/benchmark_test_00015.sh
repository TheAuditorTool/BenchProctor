#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00015() {
  user_input="$APP_INPUT"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  checked_path="/var/app/data/$(basename -- "$data")"
  echo "data" > "$checked_path"
}

benchmark_test_00015 "$@"
