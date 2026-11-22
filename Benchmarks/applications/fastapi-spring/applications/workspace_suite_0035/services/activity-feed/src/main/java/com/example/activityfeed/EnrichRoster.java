// SPDX-License-Identifier: Apache-2.0
package com.example.activityfeed;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class EnrichRoster {


    @GetMapping("/EnrichRoster/{pathId}")
    public void enrichRoster(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = pathId;
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", paragraph);
        String wording = holder.getProperty("value", "");
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(wording);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
