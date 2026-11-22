// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class VerifyThreshold {


    @PostMapping(path="/VerifyThreshold", consumes="text/plain")
    public void verifyThreshold(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = rawBody != null ? rawBody : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String consignment = transform.apply(transcript);
        if (!consignment.matches("^[a-zA-Z0-9 _.#~\\-]+$")) { response.sendError(400); return; }
        Files.write(Paths.get("/var/uploads/" + consignment), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
