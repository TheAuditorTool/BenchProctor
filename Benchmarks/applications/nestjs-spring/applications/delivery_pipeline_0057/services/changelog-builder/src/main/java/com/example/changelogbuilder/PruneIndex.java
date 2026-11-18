// SPDX-License-Identifier: Apache-2.0
package com.example.changelogbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class PruneIndex {


    @GetMapping("/PruneIndex/{pathId}")
    public void pruneIndex(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = pathId;
        String wording;
        try { wording = String.valueOf(Integer.parseInt(footnote)); }
        catch (NumberFormatException e) { wording = footnote; }
        Files.delete(Paths.get("/var/app/data/" + wording));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
