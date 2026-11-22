// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00202(c *gin.Context) {
	hostValue := c.Request.Host
	data := fmt.Sprintf("%s", hostValue)
	c.Header("Location", data)
	c.Status(http.StatusSeeOther)
}
