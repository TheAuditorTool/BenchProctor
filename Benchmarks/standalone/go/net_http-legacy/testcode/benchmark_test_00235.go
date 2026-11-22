// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00235(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	authHeader := r.Header.Get("Authorization")
	segments := strings.Split(authHeader, ",")
	data := strings.Join(segments, " ")
	tokenBytes := make([]byte, 16)
	_, err := io.ReadFull(rand.Reader, tokenBytes)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	apiToken := hex.EncodeToString(tokenBytes)
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", data, apiToken)
	RespondJSON(w, http.StatusOK, map[string]string{"token": apiToken})
}
