// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00546(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	relayPrefix := ""
	if len(forwardedIP) > 0 {
		relayPrefix = strings.ToLower(forwardedIP[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = forwardedIP
	case "f":
		data = forwardedIP
	default:
		data = forwardedIP
	}
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
