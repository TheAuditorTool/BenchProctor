// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00049(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(refererValue)
	allowedBins := map[string]bool{"ls": true, "cat": true, "date": true, "whoami": true}
	if !allowedBins[data] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	allowedBin := data
	proc, err := os.StartProcess("/bin/echo", []string{"echo", allowedBin}, &os.ProcAttr{Files: []*os.File{nil, os.Stdout, os.Stderr}})
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
