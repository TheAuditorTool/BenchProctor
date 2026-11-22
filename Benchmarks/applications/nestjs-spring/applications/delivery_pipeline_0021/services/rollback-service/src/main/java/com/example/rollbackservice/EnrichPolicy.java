// SPDX-License-Identifier: Apache-2.0
package com.example.rollbackservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class EnrichPolicy {


    @GetMapping("/EnrichPolicy")
    public void enrichPolicy(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = userAgent != null ? userAgent : "";
        java.util.function.Supplier<String> valueSupplier = () -> summary.strip();
        String phrase = valueSupplier.get();
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + phrase}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
