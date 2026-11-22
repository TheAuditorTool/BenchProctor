// SPDX-License-Identifier: Apache-2.0
package com.example.promoservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class CollectThreshold {


    @PostMapping("/CollectThreshold")
    public void collectThreshold(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = field != null ? field : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String voucher = transform.apply(subject);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(voucher).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String backorder = resolved.toString();
        String content = Files.readString(Paths.get(backorder), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
