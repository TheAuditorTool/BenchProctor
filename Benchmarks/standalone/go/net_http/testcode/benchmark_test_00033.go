// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00033(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	relayPrefix := ""
	if len(hostValue) > 0 {
		relayPrefix = strings.ToLower(hostValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = hostValue
	case "f":
		data = hostValue
	default:
		data = hostValue
	}
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
