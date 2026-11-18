// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ArchiveProfile {


    @GetMapping("/ArchiveProfile")
    public void archiveProfile(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> transcript.strip();
        String backorder = valueSupplier.get();
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + backorder}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
