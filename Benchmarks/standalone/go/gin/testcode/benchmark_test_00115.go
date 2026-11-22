// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"net/http"
	"net/url"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00115(c *gin.Context) {
	pathValue := c.Param("id")
	data, _ := url.QueryUnescape(pathValue)
	tokenLen, _ := strconv.Atoi(data)
	if tokenLen < 16 || tokenLen > 64 {
		tokenLen = 32
	}
	buf := make([]byte, tokenLen)
	rand.Read(buf)
	c.JSON(http.StatusOK, map[string]string{"token": hex.EncodeToString(buf)})
}
