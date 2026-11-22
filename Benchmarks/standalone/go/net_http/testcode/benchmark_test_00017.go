// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha512"
	"encoding/hex"
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00017(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	data := strings.Join(strings.FieldsFunc(authHeader, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	digest := sha512.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
