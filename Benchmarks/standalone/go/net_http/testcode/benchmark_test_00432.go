// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00432(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	var data string
	for _, token := range strings.Split(dbValue, ",") {
		data = token
	}
	os.Remove("/var/app/data/" + data)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
