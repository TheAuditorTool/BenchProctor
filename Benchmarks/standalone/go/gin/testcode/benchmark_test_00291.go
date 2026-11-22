// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/url"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00291(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	segments := strings.Split(headerValue, ",")
	data := strings.Join(segments, " ")
	c.Writer.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; Secure; HttpOnly; SameSite=Strict")
	c.JSON(200, gin.H{"code": "OK"})
}
