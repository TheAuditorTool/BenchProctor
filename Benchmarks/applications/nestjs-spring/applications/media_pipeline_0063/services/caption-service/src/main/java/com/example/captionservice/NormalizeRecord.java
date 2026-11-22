// SPDX-License-Identifier: Apache-2.0
package com.example.captionservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class NormalizeRecord {


    @GetMapping("/NormalizeRecord")
    public void normalizeRecord(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> snippet.strip();
        String montage = valueSupplier.get();
        new ProcessBuilder("echo", montage).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
