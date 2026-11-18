// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
)

func BenchmarkTest00018(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	content, err := os.ReadFile("/var/app/data/" + dbValue)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
