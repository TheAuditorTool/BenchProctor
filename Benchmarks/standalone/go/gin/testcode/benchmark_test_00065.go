// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00065(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	sessionCookie := &http.Cookie{Name: "session", Value: uaValue, Path: "/", Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode}
	c.Writer.Header().Add("Set-Cookie", sessionCookie.String())
	c.JSON(200, gin.H{"code": "OK"})
}
