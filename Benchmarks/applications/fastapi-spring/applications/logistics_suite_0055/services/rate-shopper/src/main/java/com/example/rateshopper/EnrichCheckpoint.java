// SPDX-License-Identifier: Apache-2.0
package com.example.rateshopper;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class EnrichCheckpoint {


    @GetMapping("/EnrichCheckpoint/{pathId}")
    public void enrichCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = pathId;
        String prefix = heading.length() > 0 ? heading.substring(0, 1).toLowerCase() : "";
        String consignment;
        switch (prefix) {
            case "h": consignment = heading.toLowerCase(); break;
            case "f": consignment = heading.toUpperCase(); break;
            default: consignment = heading.strip(); break;
        }
        Files.delete(Paths.get("/var/app/data/" + consignment));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
