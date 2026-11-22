// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00234(w http.ResponseWriter, r *http.Request) {
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
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
