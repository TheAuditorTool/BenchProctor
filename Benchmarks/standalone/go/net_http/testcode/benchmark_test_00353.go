// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"crypto/cipher"
	"crypto/des"
	"crypto/rand"
	"crypto/sha256"
	"fmt"
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00353(w http.ResponseWriter, r *http.Request) {
	pathValue := strings.TrimPrefix(r.URL.Path, "/api/")
	relayPrefix := ""
	if len(pathValue) > 0 {
		relayPrefix = strings.ToLower(pathValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = pathValue
	case "f":
		data = pathValue
	default:
		data = pathValue
	}
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
