// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"fmt"
	"io"
	"net/http"

	"golang.org/x/crypto/md4"
)

func BenchmarkTest00055(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	data := fmt.Sprintf("%s", rawBody)
	legacyDigest := md4.New()
	legacyDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(legacyDigest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
