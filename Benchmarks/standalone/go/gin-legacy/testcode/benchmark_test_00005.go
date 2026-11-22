// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00005(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	data := func(v string) string { return strings.TrimSpace(v) }(cookieValue)
	c.Writer.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; HttpOnly; SameSite=Strict")
	c.JSON(200, gin.H{"code": "OK"})
}
