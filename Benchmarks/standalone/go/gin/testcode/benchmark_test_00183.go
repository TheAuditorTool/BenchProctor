// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/url"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00183(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	data := strings.ReplaceAll(forwardedIP, "\x00", "")
	c.Writer.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; Secure; HttpOnly; SameSite=Strict")
	c.JSON(200, gin.H{"code": "OK"})
}
