// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00154(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	hexBytes, _ := hex.DecodeString(headerValue)
	data := string(hexBytes)
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
