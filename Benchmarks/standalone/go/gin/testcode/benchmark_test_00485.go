// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00485(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(jsonValue)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
