// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"crypto/sha256"
	"fmt"
	"net/http"
	"os"
	"strings"

	"golang.org/x/crypto/chacha20poly1305"
)

func BenchmarkTest00128(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	pending := strings.Split(cookieValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	aead, err := chacha20poly1305.NewX(keyHash[:])
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	nonce := make([]byte, aead.NonceSize())
	rand.Read(nonce)
	cipherOut := aead.Seal(nonce, nonce, []byte(data), nil)
	RespondJSON(w, http.StatusOK, map[string]string{"alg": "xchacha20-poly1305", "out": fmt.Sprintf("%x", cipherOut)})
}
