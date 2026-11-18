// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class FetchRecord {


    @GetMapping("/FetchRecord/{pathId}")
    public void fetchRecord(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String blurb = pathId;
        String handshake;
        try { handshake = String.valueOf(Integer.parseInt(blurb)); }
        catch (NumberFormatException e) { handshake = blurb; }
        Files.delete(Paths.get("/var/app/data/" + handshake));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
