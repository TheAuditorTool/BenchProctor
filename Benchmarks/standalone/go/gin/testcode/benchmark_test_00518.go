// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00518(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	capture := func() string { return strings.TrimSpace(forwardedIP) }
	data := capture()
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
