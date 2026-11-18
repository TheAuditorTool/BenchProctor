// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00172(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	data := strings.Join(strings.FieldsFunc(originValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	tokenLen, _ := strconv.Atoi(data)
	if tokenLen < 16 || tokenLen > 64 {
		tokenLen = 32
	}
	buf := make([]byte, tokenLen)
	rand.Read(buf)
	c.JSON(http.StatusOK, map[string]string{"token": hex.EncodeToString(buf)})
}
