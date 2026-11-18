// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"crypto/sha256"
	"fmt"
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00111(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	data := headerValue
	if _, after, ok := strings.Cut(headerValue, ","); ok {
		data = after
	}
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	cipherBlock, _ := aes.NewCipher(keyHash[:])
	gcm, _ := cipher.NewGCM(cipherBlock)
	nonce := make([]byte, gcm.NonceSize())
	rand.Read(nonce)
	cipherOut := gcm.Seal(nonce, nonce, []byte(data), nil)
	RespondJSON(w, http.StatusOK, map[string]string{"alg": "aes-gcm", "out": fmt.Sprintf("%x", cipherOut)})
}
