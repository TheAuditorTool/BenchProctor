// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00269(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	relayPrefix := ""
	if len(userID) > 0 {
		relayPrefix = strings.ToLower(userID[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = userID
	case "f":
		data = userID
	default:
		data = userID
	}
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
