// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00304(c *gin.Context) {
	fieldValue := c.PostForm("field")
	var data string
	if len(fieldValue) > 0 {
		data = fieldValue
	} else {
		data = "default"
	}
	c.Redirect(http.StatusFound, data)
}
