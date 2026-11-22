// SPDX-License-Identifier: Apache-2.0
package com.example.assetlibrary;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportArticle {


    @GetMapping("/ExportArticle")
    public void exportArticle(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> note.strip();
        String byline = valueSupplier.get();
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command("/bin/bash", "-c", "ping -c 1 -- " + byline);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
