// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00413(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	pending := strings.Split(dbValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	_lower := strings.ToLower(data)
	if !strings.HasPrefix(_lower, "t") && !strings.HasPrefix(_lower, "f") && _lower != "1" && _lower != "0" {
		c.String(http.StatusBadRequest, "invalid boolean")
		return
	}
	parsedBool := strconv.FormatBool(strings.HasPrefix(_lower, "t") || _lower == "1")
	c.Set("data", parsedBool)
}
