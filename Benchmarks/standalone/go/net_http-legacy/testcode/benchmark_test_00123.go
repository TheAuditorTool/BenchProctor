// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"crypto/aes"
	"crypto/sha256"
	"fmt"
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00123(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	multipartValue := r.FormValue("multipart_field")
	data := strings.ReplaceAll(multipartValue, "\x00", "")
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	blockCipher, err := aes.NewCipher(keyHash[:])
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	padLen := aes.BlockSize - len(data)%aes.BlockSize
	ptext := append([]byte(data), bytes.Repeat([]byte{byte(padLen)}, padLen)...)
	cipherOut := make([]byte, len(ptext))
	for off := 0; off < len(ptext); off += aes.BlockSize {
		blockCipher.Encrypt(cipherOut[off:off+aes.BlockSize], ptext[off:off+aes.BlockSize])
	}
	RespondJSON(w, http.StatusOK, map[string]string{"alg": "aes-ecb", "out": fmt.Sprintf("%x", cipherOut)})
}
