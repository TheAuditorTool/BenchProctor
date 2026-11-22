// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00176(c *gin.Context) {
	fieldValue := c.PostForm("field")
	var data string
	for _, token := range strings.Split(fieldValue, ",") {
		data = token
	}
	c.Header("Location", data)
	c.Status(http.StatusSeeOther)
}
