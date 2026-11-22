// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"crypto/sha256"
	"fmt"
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/chacha20poly1305"
)

func BenchmarkTest00132(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	segments := strings.Split(originValue, ",")
	data := strings.Join(segments, " ")
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	aead, err := chacha20poly1305.NewX(keyHash[:])
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	nonce := make([]byte, aead.NonceSize())
	rand.Read(nonce)
	cipherOut := aead.Seal(nonce, nonce, []byte(data), nil)
	c.JSON(http.StatusOK, map[string]string{"alg": "xchacha20-poly1305", "out": fmt.Sprintf("%x", cipherOut)})
}
