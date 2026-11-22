// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/url"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00019(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	relayPrefix := ""
	if len(headerValue) > 0 {
		relayPrefix = strings.ToLower(headerValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = headerValue
	case "f":
		data = headerValue
	default:
		data = headerValue
	}
	c.Writer.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; Secure; HttpOnly; SameSite=Strict")
	c.JSON(200, gin.H{"code": "OK"})
}
