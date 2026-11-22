// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00199(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	relayPrefix := ""
	if len(authHeader) > 0 {
		relayPrefix = strings.ToLower(authHeader[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = authHeader
	case "f":
		data = authHeader
	default:
		data = authHeader
	}
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
