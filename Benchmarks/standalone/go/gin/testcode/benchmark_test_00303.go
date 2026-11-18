// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"crypto/sha256"
	"fmt"
	"io"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00303(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	var data string
	if len(rawBody) > 0 {
		data = rawBody
	} else {
		data = "default"
	}
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	cipherBlock, _ := aes.NewCipher(keyHash[:])
	gcm, _ := cipher.NewGCM(cipherBlock)
	nonce := make([]byte, gcm.NonceSize())
	rand.Read(nonce)
	cipherOut := gcm.Seal(nonce, nonce, []byte(data), nil)
	c.JSON(http.StatusOK, map[string]string{"alg": "aes-gcm", "out": fmt.Sprintf("%x", cipherOut)})
}
