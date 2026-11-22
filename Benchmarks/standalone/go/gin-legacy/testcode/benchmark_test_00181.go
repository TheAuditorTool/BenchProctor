// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00181(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var data string
	for _, token := range strings.Split(commentText, ",") {
		data = token
	}
	c.Header("Location", data)
	c.Status(http.StatusSeeOther)
}
