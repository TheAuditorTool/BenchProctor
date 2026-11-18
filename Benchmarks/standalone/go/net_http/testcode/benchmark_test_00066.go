// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00066(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(dbValue)
	http.Redirect(w, r, data, http.StatusFound)
}
