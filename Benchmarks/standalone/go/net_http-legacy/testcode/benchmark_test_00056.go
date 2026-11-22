// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"regexp"
)

func BenchmarkTest00056(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(commentText) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := commentText
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, processed))
}
