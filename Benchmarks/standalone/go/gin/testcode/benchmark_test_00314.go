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

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00314(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	data := strings.ReplaceAll(cookieValue, "\x00", "")
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	cipherBlock, _ := des.NewTripleDESCipher(keyHash[:24])
	iv := make([]byte, des.BlockSize)
	rand.Read(iv)
	padLen := des.BlockSize - len(data)%des.BlockSize
	ptext := append([]byte(data), bytes.Repeat([]byte{byte(padLen)}, padLen)...)
	cipherOut := make([]byte, len(ptext))
	cipher.NewCBCEncrypter(cipherBlock, iv).CryptBlocks(cipherOut, ptext)
	c.JSON(http.StatusOK, map[string]string{"alg": "3des-cbc", "out": fmt.Sprintf("%x%x", iv, cipherOut)})
}
