// SPDX-License-Identifier: Apache-2.0
package com.example.supplierfeed;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ResolveSnapshot {


    @PostMapping(path="/ResolveSnapshot", consumes="text/plain")
    public void resolveSnapshot(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = rawBody != null ? rawBody : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String backorder = transform.apply(memo);
        if (!backorder.matches("^[a-zA-Z0-9 _.#~\\-]+$")) { response.sendError(400); return; }
        Files.write(Paths.get("/var/uploads/" + backorder), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
