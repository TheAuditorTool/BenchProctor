// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha512"
	"encoding/hex"
	"io"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00072(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	data := strings.Join(strings.FieldsFunc(authHeader, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	digest := sha512.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
