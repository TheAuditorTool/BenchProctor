// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00558(w http.ResponseWriter, r *http.Request) {
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
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
