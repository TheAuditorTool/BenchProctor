// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00116(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	relayPrefix := ""
	if len(authHeader) > 0 {
		relayPrefix = strings.ToLower(authHeader[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = authHeader
	case "f":
		data = authHeader
	default:
		data = authHeader
	}
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
