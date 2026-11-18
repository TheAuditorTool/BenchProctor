// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00454(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	data := headerValue
	if _, after, ok := strings.Cut(headerValue, ","); ok {
		data = after
	}
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: data, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
