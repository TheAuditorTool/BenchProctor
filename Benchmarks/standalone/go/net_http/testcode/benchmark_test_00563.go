// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
)

func BenchmarkTest00563(w http.ResponseWriter, r *http.Request) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var data string
	if commentText != "" {
		data = commentText
	}
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
