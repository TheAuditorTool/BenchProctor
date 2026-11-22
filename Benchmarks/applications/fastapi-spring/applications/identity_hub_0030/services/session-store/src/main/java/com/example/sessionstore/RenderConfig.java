// SPDX-License-Identifier: Apache-2.0
package com.example.sessionstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@RestController
class RenderConfig {


    @GetMapping("/RenderConfig")
    public void renderConfig(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = authorization != null ? authorization : "";
        String prefix = tagline.length() > 0 ? tagline.substring(0, 1).toLowerCase() : "";
        String persona;
        switch (prefix) {
            case "h": persona = tagline.toLowerCase(); break;
            case "f": persona = tagline.toUpperCase(); break;
            default: persona = tagline.strip(); break;
        }
        String socketRaw = String.valueOf(persona);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
