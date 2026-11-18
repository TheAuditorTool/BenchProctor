// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00244(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	segments := strings.Split(dbValue, ",")
	data := strings.Join(segments, " ")
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
