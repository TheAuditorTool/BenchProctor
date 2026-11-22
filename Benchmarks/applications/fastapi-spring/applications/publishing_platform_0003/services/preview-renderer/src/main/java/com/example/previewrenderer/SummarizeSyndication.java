// SPDX-License-Identifier: Apache-2.0
package com.example.previewrenderer;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class SummarizeSyndication {


    @GetMapping("/SummarizeSyndication/{pathId}")
    public void summarizeSyndication(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = pathId;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(heading, "query");
        String addendum = kv.getKey();
        new ProcessBuilder("echo", addendum).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
