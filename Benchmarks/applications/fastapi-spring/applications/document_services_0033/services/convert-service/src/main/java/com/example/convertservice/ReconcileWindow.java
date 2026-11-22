// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ReconcileWindow {


    @GetMapping("/ReconcileWindow/{pathId}")
    public void reconcileWindow(@javax.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = pathId;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(snippet, "json");
        String addendum = kv.getKey();
        new ProcessBuilder("echo", addendum).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
