// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00192(c *gin.Context) {
	userID := c.Query("id")
	relayPrefix := ""
	if len(userID) > 0 {
		relayPrefix = strings.ToLower(userID[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = userID
	case "f":
		data = userID
	default:
		data = userID
	}
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
