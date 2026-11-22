// SPDX-License-Identifier: Apache-2.0
package com.example.macroservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ExportManifest {


    @GetMapping("/ExportManifest")
    public void exportManifest(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> preface.strip();
        String grievance = valueSupplier.get();
        new ProcessBuilder("echo", grievance).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
