// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/microcosm-cc/bluemonday"
)

func BenchmarkTest00020(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	var data string
	if len(dbValue) > 0 {
		data = dbValue
	} else {
		data = "default"
	}
	processed := bluemonday.UGCPolicy().Sanitize(data)
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
