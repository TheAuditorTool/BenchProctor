// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00357(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	data, _ := url.QueryUnescape(cookieValue)
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: data, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
