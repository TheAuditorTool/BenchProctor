// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class AuditBundle {


    @GetMapping("/AuditBundle")
    public void auditBundle(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = authorization != null ? authorization : "";
        String prefix = paragraph.length() > 0 ? paragraph.substring(0, 1).toLowerCase() : "";
        String gauge;
        switch (prefix) {
            case "h": gauge = paragraph.toLowerCase(); break;
            case "f": gauge = paragraph.toUpperCase(); break;
            default: gauge = paragraph.strip(); break;
        }
        Files.delete(Paths.get("/var/app/data/" + gauge));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
