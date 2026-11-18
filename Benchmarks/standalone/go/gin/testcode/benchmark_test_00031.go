// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00031(c *gin.Context) {
	val := rand.Intn(1000000)
	c.JSON(http.StatusOK, map[string]string{"token": fmt.Sprintf("%d", val)})
}
