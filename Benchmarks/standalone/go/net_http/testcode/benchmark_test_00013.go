// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"strings"
)

func BenchmarkTest00013(w http.ResponseWriter, r *http.Request) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	relayPrefix := ""
	if len(commentText) > 0 {
		relayPrefix = strings.ToLower(commentText[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = commentText
	case "f":
		data = commentText
	default:
		data = commentText
	}
	w.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; HttpOnly; SameSite=Strict")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
