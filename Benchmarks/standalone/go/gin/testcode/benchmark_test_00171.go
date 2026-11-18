// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00171(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	htmlOut := "<div>" + authHeader + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
