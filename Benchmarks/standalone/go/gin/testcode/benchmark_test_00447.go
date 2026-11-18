// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00447(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	data := forwardedIP
	if _, after, ok := strings.Cut(forwardedIP, ","); ok {
		data = after
	}
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
