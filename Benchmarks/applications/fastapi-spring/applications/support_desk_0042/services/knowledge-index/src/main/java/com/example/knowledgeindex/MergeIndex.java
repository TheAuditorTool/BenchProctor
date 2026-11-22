// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class MergeIndex {


    @GetMapping("/MergeIndex/{pathId}")
    public void mergeIndex(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String blurb = pathId;
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(blurb, "form");
        String inquiry = entry.getKey();
        new ProcessBuilder("echo", inquiry).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
