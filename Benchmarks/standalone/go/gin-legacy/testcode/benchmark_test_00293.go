// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00293(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(commentText) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := commentText
	c.Set("data", processed)
}
