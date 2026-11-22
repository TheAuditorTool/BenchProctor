// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"

	"golang.org/x/crypto/sha3"
)

func BenchmarkTest00063(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	userID := r.URL.Query().Get("id")
	var data string
	if len(userID) > 0 {
		data = userID
	} else {
		data = "default"
	}
	strongDigest := sha3.New256()
	strongDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(strongDigest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
