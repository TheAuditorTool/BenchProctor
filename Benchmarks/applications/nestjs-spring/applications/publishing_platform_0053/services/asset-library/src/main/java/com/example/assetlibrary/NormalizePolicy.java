// SPDX-License-Identifier: Apache-2.0
package com.example.assetlibrary;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class NormalizePolicy {


    @GetMapping("/NormalizePolicy")
    public void normalizePolicy(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = authorization != null ? authorization : "";
        String byline = note.isEmpty() ? "default" : note;
        String addendum = byline.matches("^(status|info|list|show)$") ? byline : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + addendum});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
