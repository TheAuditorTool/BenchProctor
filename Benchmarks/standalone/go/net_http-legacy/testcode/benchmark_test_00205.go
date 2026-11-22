// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00205(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var data string
	if len(commentText) > 0 {
		data = commentText
	} else {
		data = "default"
	}
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
