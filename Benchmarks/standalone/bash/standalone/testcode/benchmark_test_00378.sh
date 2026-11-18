#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00378() {
  user_input="$UPLOAD_NAME"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00378 "$@"
