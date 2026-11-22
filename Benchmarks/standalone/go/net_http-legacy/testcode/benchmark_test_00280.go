// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os"
	"strconv"
	"strings"
)

func BenchmarkTest00280(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	headerValue := r.Header.Get("X-Custom-Header")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", headerValue)
	data := relayBuilder.String()
	proc, err := os.StartProcess("/bin/sh", []string{"sh", "-c", "echo " + data}, &os.ProcAttr{Files: []*os.File{nil, os.Stdout, os.Stderr}})
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	procState, err := proc.Wait()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	RespondJSON(w, http.StatusOK, map[string]string{"exit": strconv.Itoa(procState.ExitCode())})
}
