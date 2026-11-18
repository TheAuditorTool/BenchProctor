// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00317(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	data := strings.Join(strings.FieldsFunc(multipartValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	c.JSON(http.StatusOK, map[string]string{"name": *result})
}
