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

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00045(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var data string
	if commentText != "" {
		data = commentText
	}
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	salt := make([]byte, 16)
	rand.Read(salt)
	messageKey := hmac.New(sha256.New, keyHash[:])
	messageKey.Write(salt)
	streamCipher, err := rc4.NewCipher(messageKey.Sum(nil)[:16])
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	cipherOut := make([]byte, len(data))
	streamCipher.XORKeyStream(cipherOut, []byte(data))
	cipherOut = append(salt, cipherOut...)
	c.JSON(http.StatusOK, map[string]string{"alg": "rc4", "out": fmt.Sprintf("%x", cipherOut)})
}
