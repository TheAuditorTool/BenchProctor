// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00358(c *gin.Context) {
	_apiResp, _apiErr := http.Get("https://api.svc.cluster/data")
	if _apiErr != nil {
		return
	}
	defer _apiResp.Body.Close()
	_apiBytes, _ := io.ReadAll(_apiResp.Body)
	apiValue := string(_apiBytes)
	data := fmt.Sprintf("%s", apiValue)
	c.Redirect(http.StatusFound, data)
}
