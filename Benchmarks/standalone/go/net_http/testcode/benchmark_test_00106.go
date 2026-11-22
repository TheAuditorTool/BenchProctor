// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strconv"
)

func BenchmarkTest00106(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	var data string
	if refererValue != "" {
		data = refererValue
	}
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
