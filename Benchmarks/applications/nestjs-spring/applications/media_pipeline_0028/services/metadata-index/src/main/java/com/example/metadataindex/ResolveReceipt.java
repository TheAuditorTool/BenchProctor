// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ResolveReceipt {


    @GetMapping("/ResolveReceipt")
    public void resolveReceipt(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = host != null ? host : "";
        String rendition = citation.isEmpty() ? "default" : citation;
        String montage = rendition.matches("^(config|data|index|schema)$") ? rendition : "config";
        Files.write(Paths.get("/var/uploads/" + montage), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
