// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha1"
	"encoding/hex"
	"io"
	"net/http"
)

func BenchmarkTest00264(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	fieldValue := r.FormValue("field")
	var data string
	if fieldValue != "" {
		data = fieldValue
	}
	digest := sha1.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
