// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00145(c *gin.Context) {
	_apiResp, _apiErr := http.Get("https://api.svc.cluster/data")
	if _apiErr != nil {
		return
	}
	defer _apiResp.Body.Close()
	_apiBytes, _ := ioutil.ReadAll(_apiResp.Body)
	apiValue := string(_apiBytes)
	pending := strings.Split(apiValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	http.RedirectHandler(data, http.StatusFound).ServeHTTP(c.Writer, c.Request)
}
