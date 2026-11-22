// SPDX-License-Identifier: Apache-2.0
package com.example.shareservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class MergeLedger {


    @PostMapping(path="/MergeLedger", consumes="text/plain")
    public void mergeLedger(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = rawBody != null ? rawBody : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String synopsis = transform.apply(caption);
        if (!synopsis.matches("^[a-zA-Z0-9 _.#~\\-]+$")) { response.sendError(400); return; }
        Files.write(Paths.get("/var/uploads/" + synopsis), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
