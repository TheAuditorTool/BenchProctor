// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00305(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	segments := strings.Split(uaValue, ",")
	data := strings.Join(segments, " ")
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
