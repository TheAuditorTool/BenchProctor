// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"crypto/aes"
	"crypto/sha256"
	"fmt"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00067(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	keyHash := sha256.Sum256([]byte(os.Getenv("DATA_ENC_KEY")))
	blockCipher, err := aes.NewCipher(keyHash[:])
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	padLen := aes.BlockSize - len(commentText)%aes.BlockSize
	ptext := append([]byte(commentText), bytes.Repeat([]byte{byte(padLen)}, padLen)...)
	cipherOut := make([]byte, len(ptext))
	for off := 0; off < len(ptext); off += aes.BlockSize {
		blockCipher.Encrypt(cipherOut[off:off+aes.BlockSize], ptext[off:off+aes.BlockSize])
	}
	c.JSON(http.StatusOK, map[string]string{"alg": "aes-ecb", "out": fmt.Sprintf("%x", cipherOut)})
}
