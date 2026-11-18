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
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00220(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	xmlBody := string(rawBytes)
	capture := func() string { return strings.TrimSpace(xmlBody) }
	data := capture()
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	cipherBlock, _ := aes.NewCipher(keyHash[:])
	gcm, _ := cipher.NewGCM(cipherBlock)
	nonce := make([]byte, gcm.NonceSize())
	rand.Read(nonce)
	cipherOut := gcm.Seal(nonce, nonce, []byte(data), nil)
	c.JSON(http.StatusOK, map[string]string{"alg": "aes-gcm", "out": fmt.Sprintf("%x", cipherOut)})
}
