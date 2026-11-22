// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00237(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	relayPrefix := ""
	if len(uaValue) > 0 {
		relayPrefix = strings.ToLower(uaValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = uaValue
	case "f":
		data = uaValue
	default:
		data = uaValue
	}
	sessionCookie := &http.Cookie{Name: "session", Value: data, Path: "/", Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode}
	c.Writer.Header().Add("Set-Cookie", sessionCookie.String())
	c.JSON(200, gin.H{"code": "OK"})
}
