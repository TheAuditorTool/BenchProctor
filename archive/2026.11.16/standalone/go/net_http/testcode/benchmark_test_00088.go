// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00088(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	data := strings.Join(strings.FieldsFunc(userID, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	tokenLen, _ := strconv.Atoi(data)
	if tokenLen < 16 || tokenLen > 64 {
		tokenLen = 32
	}
	buf := make([]byte, tokenLen)
	rand.Read(buf)
	RespondJSON(w, http.StatusOK, map[string]string{"token": hex.EncodeToString(buf)})
}
