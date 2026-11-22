// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00149(c *gin.Context) {
	fieldValue := c.PostForm("field")
	data := strings.ReplaceAll(fieldValue, "\x00", "")
	c.Header("Location", data)
	c.Status(http.StatusSeeOther)
}
