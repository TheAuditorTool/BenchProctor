// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00074(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	capture := func() string { return strings.TrimSpace(authHeader) }
	data := capture()
	sessionCookie := &http.Cookie{Name: "session", Value: data, Path: "/", HttpOnly: true, SameSite: http.SameSiteStrictMode}
	c.Writer.Header().Add("Set-Cookie", sessionCookie.String())
	c.JSON(200, gin.H{"code": "OK"})
}
