// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00002(c *gin.Context) {
	userID := c.Query("id")
	var data string
	if len(userID) > 0 {
		data = userID
	} else {
		data = "default"
	}
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	c.JSON(http.StatusOK, map[string]string{"name": *result})
}
