// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/hmac"
	"crypto/rand"
	"crypto/rc4"
	"crypto/sha256"
	"fmt"
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00271(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	var data string
	for _, token := range strings.Split(multipartValue, ",") {
		data = token
	}
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	salt := make([]byte, 16)
	rand.Read(salt)
	messageKey := hmac.New(sha256.New, keyHash[:])
	messageKey.Write(salt)
	streamCipher, err := rc4.NewCipher(messageKey.Sum(nil)[:16])
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	cipherOut := make([]byte, len(data))
	streamCipher.XORKeyStream(cipherOut, []byte(data))
	cipherOut = append(salt, cipherOut...)
	RespondJSON(w, http.StatusOK, map[string]string{"alg": "rc4", "out": fmt.Sprintf("%x", cipherOut)})
}
