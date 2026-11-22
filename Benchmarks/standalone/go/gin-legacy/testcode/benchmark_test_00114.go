// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"os/exec"
	"regexp"
	"time"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00114(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(jsonValue) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := jsonValue
	scriptCtx, cancelScript := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancelScript()
	cmd := exec.CommandContext(scriptCtx, "python3", "-c", processed)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
