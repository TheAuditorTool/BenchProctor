// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/microcosm-cc/bluemonday"
)

func BenchmarkTest00010(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	data := func(v string) string { return strings.TrimSpace(v) }(dbValue)
	processed := bluemonday.UGCPolicy().Sanitize(data)
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
