// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
	"strings"

	"golang.org/x/crypto/md4"
)

func BenchmarkTest00074(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	fieldValue := r.FormValue("field")
	relayPrefix := ""
	if len(fieldValue) > 0 {
		relayPrefix = strings.ToLower(fieldValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = fieldValue
	case "f":
		data = fieldValue
	default:
		data = fieldValue
	}
	legacyDigest := md4.New()
	legacyDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(legacyDigest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
