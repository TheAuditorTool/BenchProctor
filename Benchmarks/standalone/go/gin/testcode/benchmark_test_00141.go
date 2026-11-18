// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00141(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(headerValue)
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: data, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
