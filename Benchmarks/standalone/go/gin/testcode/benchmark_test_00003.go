// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00003(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	pending := strings.Split(commentText, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	c.JSON(http.StatusOK, map[string]string{"name": *result})
}
