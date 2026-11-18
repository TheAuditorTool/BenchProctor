// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"crypto/sha256"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00216(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	data := strings.ReplaceAll(jsonValue, "\x00", "")
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	cipherBlock, _ := aes.NewCipher(keyHash[:])
	gcm, _ := cipher.NewGCM(cipherBlock)
	nonce := make([]byte, gcm.NonceSize())
	rand.Read(nonce)
	cipherOut := gcm.Seal(nonce, nonce, []byte(data), nil)
	RespondJSON(w, http.StatusOK, map[string]string{"alg": "aes-gcm", "out": fmt.Sprintf("%x", cipherOut)})
}
