// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class CompactWindow {


    @GetMapping("/CompactWindow/{pathId}")
    public void compactWindow(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = pathId;
        String prefix = citation.length() > 0 ? citation.substring(0, 1).toLowerCase() : "";
        String backorder;
        switch (prefix) {
            case "h": backorder = citation.toLowerCase(); break;
            case "f": backorder = citation.toUpperCase(); break;
            default: backorder = citation.strip(); break;
        }
        Files.delete(Paths.get("/var/app/data/" + backorder));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
