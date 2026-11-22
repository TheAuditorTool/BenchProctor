// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha3"
	"encoding/hex"
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00088(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	xmlBody := string(rawBytes)
	segments := strings.Split(xmlBody, ",")
	data := strings.Join(segments, " ")
	strongDigest := sha3.New256()
	strongDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(strongDigest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
