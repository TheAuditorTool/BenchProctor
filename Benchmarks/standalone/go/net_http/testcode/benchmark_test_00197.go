// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strings"
)

func BenchmarkTest00197(w http.ResponseWriter, r *http.Request) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var data string
	for _, token := range strings.Split(commentText, ",") {
		data = token
	}
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
