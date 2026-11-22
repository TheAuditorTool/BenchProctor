// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha512"
	"encoding/hex"
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00074(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	segments := strings.Split(hostValue, ",")
	data := strings.Join(segments, " ")
	digest := sha512.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
