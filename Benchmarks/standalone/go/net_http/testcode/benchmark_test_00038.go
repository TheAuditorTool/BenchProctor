// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00038(w http.ResponseWriter, r *http.Request) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	data := strings.ReplaceAll(commentText, "\x00", "")
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	RespondJSON(w, http.StatusOK, map[string]string{"name": *result})
}
