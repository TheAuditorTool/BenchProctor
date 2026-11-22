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

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00248(c *gin.Context) {
	userID := c.Query("id")
	data := fmt.Sprintf("%s", userID)
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	blockCipher, err := aes.NewCipher(keyHash[:])
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	gcm, err := cipher.NewGCM(blockCipher)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	nonce := make([]byte, gcm.NonceSize())
	rand.Read(nonce)
	cipherOut := gcm.Seal(nonce, nonce, []byte(data), nil)
	c.JSON(http.StatusOK, map[string]string{"alg": "aes-gcm", "out": fmt.Sprintf("%x", cipherOut)})
}
