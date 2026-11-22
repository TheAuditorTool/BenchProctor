// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00297(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	data := fmt.Sprintf("%s", commentText)
	c.Header("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(c.Writer, "<p>Results for %s</p>", data)
}
