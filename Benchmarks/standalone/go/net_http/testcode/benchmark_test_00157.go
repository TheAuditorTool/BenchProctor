// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"crypto/cipher"
	"crypto/des"
	"crypto/rand"
	"crypto/sha256"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00157(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", jsonValue)
	data := relayBuilder.String()
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	cipherBlock, _ := des.NewTripleDESCipher(keyHash[:24])
	iv := make([]byte, des.BlockSize)
	rand.Read(iv)
	padLen := des.BlockSize - len(data)%des.BlockSize
	ptext := append([]byte(data), bytes.Repeat([]byte{byte(padLen)}, padLen)...)
	cipherOut := make([]byte, len(ptext))
	cipher.NewCBCEncrypter(cipherBlock, iv).CryptBlocks(cipherOut, ptext)
	RespondJSON(w, http.StatusOK, map[string]string{"alg": "3des-cbc", "out": fmt.Sprintf("%x%x", iv, cipherOut)})
}
