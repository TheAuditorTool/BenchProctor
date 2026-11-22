// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
	"strings"

	"golang.org/x/crypto/md4"
)

func BenchmarkTest00230(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	forwardedIP := r.Header.Get("X-Forwarded-For")
	segments := strings.Split(forwardedIP, ",")
	data := strings.Join(segments, " ")
	legacyDigest := md4.New()
	legacyDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(legacyDigest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
