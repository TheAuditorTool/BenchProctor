// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00568(w http.ResponseWriter, r *http.Request) {
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
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
