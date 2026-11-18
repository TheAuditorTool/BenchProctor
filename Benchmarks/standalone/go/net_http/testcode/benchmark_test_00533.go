// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00533(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data := strings.ReplaceAll(refererValue, "\x00", "")
	tokenLen, _ := strconv.Atoi(data)
	if tokenLen < 16 || tokenLen > 64 {
		tokenLen = 32
	}
	buf := make([]byte, tokenLen)
	rand.Read(buf)
	RespondJSON(w, http.StatusOK, map[string]string{"token": hex.EncodeToString(buf)})
}
