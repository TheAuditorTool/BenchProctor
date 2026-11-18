// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00532(c *gin.Context) {
	hostValue := c.Request.Host
	relayPrefix := ""
	if len(hostValue) > 0 {
		relayPrefix = strings.ToLower(hostValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = hostValue
	case "f":
		data = hostValue
	default:
		data = hostValue
	}
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
