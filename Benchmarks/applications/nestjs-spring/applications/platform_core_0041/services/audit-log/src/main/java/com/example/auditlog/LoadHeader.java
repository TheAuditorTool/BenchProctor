// SPDX-License-Identifier: Apache-2.0
package com.example.auditlog;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@RestController
class LoadHeader {


    @GetMapping("/LoadHeader")
    public void loadHeader(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = xCustomHeader != null ? xCustomHeader : "";
        String prefix = passage.length() > 0 ? passage.substring(0, 1).toLowerCase() : "";
        String persona;
        switch (prefix) {
            case "h": persona = passage.toLowerCase(); break;
            case "f": persona = passage.toUpperCase(); break;
            default: persona = passage.strip(); break;
        }
        String socketRaw = String.valueOf(persona);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
