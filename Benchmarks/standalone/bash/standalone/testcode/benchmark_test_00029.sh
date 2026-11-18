#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00029() {
  user_input="$UPLOAD_NAME"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  checked_path=$(realpath -m "/var/app/data/$data")
  if [[ ! "$checked_path" == /var/app/data/* ]]; then echo "forbidden" >&2; exit 1; fi
  echo "data" > "$checked_path"
}

benchmark_test_00029 "$@"
