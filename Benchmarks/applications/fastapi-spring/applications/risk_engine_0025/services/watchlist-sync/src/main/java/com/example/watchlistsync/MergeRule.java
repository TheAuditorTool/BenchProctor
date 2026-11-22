// SPDX-License-Identifier: Apache-2.0
package com.example.watchlistsync;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class MergeRule {


    @PostMapping(path="/MergeRule", consumes="text/plain")
    public void mergeRule(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = rawBody != null ? rawBody : "";
        java.util.function.Supplier<String> valueSupplier = () -> excerpt.strip();
        String verdict = valueSupplier.get();
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + verdict});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
