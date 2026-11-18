// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00151(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	var data string
	for _, token := range strings.Split(dbValue, ",") {
		data = token
	}
	c.Set("data", data)
}
