// SPDX-License-Identifier: Apache-2.0
package com.example.documentapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class AuditBatch {


    @GetMapping("/AuditBatch")
    public void auditBatch(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = authorization != null ? authorization : "";
        String prefix = wording.length() > 0 ? wording.substring(0, 1).toLowerCase() : "";
        String addendum;
        switch (prefix) {
            case "h": addendum = wording.toLowerCase(); break;
            case "f": addendum = wording.toUpperCase(); break;
            default: addendum = wording.strip(); break;
        }
        Files.delete(Paths.get("/var/app/data/" + addendum));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
