// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00036(c *gin.Context) {
	fieldValue := c.PostForm("field")
	data := fieldValue
	if _, after, ok := strings.Cut(fieldValue, ","); ok {
		data = after
	}
	_lower := strings.ToLower(data)
	if !strings.HasPrefix(_lower, "t") && !strings.HasPrefix(_lower, "f") && _lower != "1" && _lower != "0" {
		c.String(http.StatusBadRequest, "invalid boolean")
		return
	}
	parsedBool := strconv.FormatBool(strings.HasPrefix(_lower, "t") || _lower == "1")
	c.Set("data", parsedBool)
}
