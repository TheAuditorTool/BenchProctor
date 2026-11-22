// SPDX-License-Identifier: Apache-2.0
package com.example.previewrenderer;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class EnrichBundle {


    @PostMapping(path="/EnrichBundle", consumes="text/plain")
    public void enrichBundle(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = rawBody != null ? rawBody : "";
        java.util.function.Supplier<String> valueSupplier = () -> synopsis.strip();
        String byline = valueSupplier.get();
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + byline});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
