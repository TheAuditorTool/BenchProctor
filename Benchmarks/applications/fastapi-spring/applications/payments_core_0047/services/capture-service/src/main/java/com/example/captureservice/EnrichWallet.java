// SPDX-License-Identifier: Apache-2.0
package com.example.captureservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class EnrichWallet {


    @PostMapping("/EnrichWallet")
    public void enrichWallet(@javax.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = field != null ? field : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String remittance = transform.apply(footnote);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(remittance).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String disbursement = resolved.toString();
        String content = Files.readString(Paths.get(disbursement), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
