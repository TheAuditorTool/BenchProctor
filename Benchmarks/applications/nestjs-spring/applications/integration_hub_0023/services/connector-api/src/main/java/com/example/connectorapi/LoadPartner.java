// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class LoadPartner {


    @GetMapping("/LoadPartner")
    public void loadPartner(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = host != null ? host : "";
        String handshake = caption.isEmpty() ? "default" : caption;
        String subject = handshake.matches("^(config|data|index|schema)$") ? handshake : "config";
        Files.write(Paths.get("/var/uploads/" + subject), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
