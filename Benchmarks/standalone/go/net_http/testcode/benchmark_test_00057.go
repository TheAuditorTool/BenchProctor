// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
	"strings"

	"golang.org/x/crypto/md4"
)

func BenchmarkTest00057(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	data := hostValue
	if _, after, ok := strings.Cut(hostValue, ","); ok {
		data = after
	}
	legacyDigest := md4.New()
	legacyDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(legacyDigest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
