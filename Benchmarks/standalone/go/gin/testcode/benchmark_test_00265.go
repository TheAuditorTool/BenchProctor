// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00265(c *gin.Context) {
	pathValue := c.Param("id")
	var data string
	if len(pathValue) > 0 {
		data = pathValue
	} else {
		data = "default"
	}
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
