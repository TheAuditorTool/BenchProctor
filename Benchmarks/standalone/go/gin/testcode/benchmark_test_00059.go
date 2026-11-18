// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00059(c *gin.Context) {
	pathValue := c.Param("id")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(pathValue)
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
