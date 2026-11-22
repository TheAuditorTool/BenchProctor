// SPDX-License-Identifier: Apache-2.0
package com.example.syndicationfeed;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class SummarizeConfig {


    @GetMapping("/SummarizeConfig/{pathId}")
    public void summarizeConfig(@javax.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = pathId;
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(transcript, "http");
        String addendum = pair.getKey();
        new ProcessBuilder("echo", addendum).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
