#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00117() {
  user_input="`curl -s http://169.254.169.254/latest/meta-data/`"
  printf -v data "%s" "${user_input}"
  psql "$DATABASE_URL" -qAt -c "PREPARE user_lookup AS SELECT * FROM users WHERE id = '$data'; EXECUTE user_lookup;"
}

benchmark_test_00117 "$@"
