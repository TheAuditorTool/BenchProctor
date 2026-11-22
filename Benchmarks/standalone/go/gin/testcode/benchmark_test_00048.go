// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/url"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00048(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	relayPrefix := ""
	if len(commentText) > 0 {
		relayPrefix = strings.ToLower(commentText[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = commentText
	case "f":
		data = commentText
	default:
		data = commentText
	}
	c.Writer.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; HttpOnly; SameSite=Strict")
	c.JSON(200, gin.H{"code": "OK"})
}
