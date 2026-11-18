// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
)

func BenchmarkTest00028(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(dbValue)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
