// SPDX-License-Identifier: Apache-2.0
package com.example.indexbuilder;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class PublishManifest {


    @PostMapping(path="/PublishManifest", consumes="text/plain")
    public void publishManifest(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = rawBody != null ? rawBody : "";
        String dossier;
        if (citation.length() > 256) { dossier = citation.substring(0, 256); }
        else { dossier = citation; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(dossier)) { response.sendError(403); return; }
        String addendum = dossier;
        Runtime.getRuntime().exec(new String[]{addendum}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
