// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00142(c *gin.Context) {
	userID := c.Query("id")
	var data string
	for _, token := range strings.Split(userID, ",") {
		data = token
	}
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
