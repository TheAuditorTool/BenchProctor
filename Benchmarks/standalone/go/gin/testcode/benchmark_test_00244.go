// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00244(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var data string
	if commentText != "" {
		data = commentText
	}
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
