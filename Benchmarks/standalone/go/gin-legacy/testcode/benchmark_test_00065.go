// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00065(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", commentText)
	data := relayBuilder.String()
	sessionCookie := &http.Cookie{Name: "session", Value: data, Path: "/", Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode}
	c.Writer.Header().Add("Set-Cookie", sessionCookie.String())
	c.JSON(200, gin.H{"code": "OK"})
}
