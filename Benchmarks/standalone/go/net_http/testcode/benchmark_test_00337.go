// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"crypto/cipher"
	"crypto/des"
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"net/http"
	"os"
)

func BenchmarkTest00337(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	hexBytes, _ := hex.DecodeString(cookieValue)
	data := string(hexBytes)
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
