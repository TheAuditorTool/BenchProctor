// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/url"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00244(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	data := originValue
	if _, after, ok := strings.Cut(originValue, ","); ok {
		data = after
	}
	c.Writer.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; Secure; HttpOnly; SameSite=Strict")
	c.JSON(200, gin.H{"code": "OK"})
}
