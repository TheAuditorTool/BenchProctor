// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00226(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", headerValue)
	data := relayBuilder.String()
	proc, err := os.StartProcess("/bin/sh", []string{"sh", "-c", "echo " + data}, &os.ProcAttr{Files: []*os.File{nil, os.Stdout, os.Stderr}})
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	procState, err := proc.Wait()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(http.StatusOK, map[string]string{"exit": strconv.Itoa(procState.ExitCode())})
}
