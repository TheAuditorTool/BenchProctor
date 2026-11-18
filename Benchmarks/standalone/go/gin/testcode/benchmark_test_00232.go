// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00232(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	relayPrefix := ""
	if len(forwardedIP) > 0 {
		relayPrefix = strings.ToLower(forwardedIP[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = forwardedIP
	case "f":
		data = forwardedIP
	default:
		data = forwardedIP
	}
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
