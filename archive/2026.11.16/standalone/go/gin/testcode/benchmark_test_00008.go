// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00008(c *gin.Context) {
	fieldValue := c.PostForm("field")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(fieldValue)
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
