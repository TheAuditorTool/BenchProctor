// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha1"
	"encoding/hex"
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00124(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(userID)
	digest := sha1.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
