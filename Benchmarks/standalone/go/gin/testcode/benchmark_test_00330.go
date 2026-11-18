// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00330(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: headerValue, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
