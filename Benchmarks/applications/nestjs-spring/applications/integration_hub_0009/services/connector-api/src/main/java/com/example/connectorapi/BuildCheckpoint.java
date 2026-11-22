// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class BuildCheckpoint {


    @GetMapping("/BuildCheckpoint")
    public void buildCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = authorization != null ? authorization : "";
        String prefix = heading.length() > 0 ? heading.substring(0, 1).toLowerCase() : "";
        String handshake;
        switch (prefix) {
            case "h": handshake = heading.toLowerCase(); break;
            case "f": handshake = heading.toUpperCase(); break;
            default: handshake = heading.strip(); break;
        }
        Files.delete(Paths.get("/var/app/data/" + handshake));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
