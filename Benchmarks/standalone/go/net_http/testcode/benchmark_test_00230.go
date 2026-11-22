// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha1"
	"encoding/hex"
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00230(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	var data string
	for _, token := range strings.Split(uaValue, ",") {
		data = token
	}
	digest := sha1.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
