// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00301(c *gin.Context) {
	pathValue := c.Param("id")
	c.Redirect(http.StatusFound, pathValue)
}
