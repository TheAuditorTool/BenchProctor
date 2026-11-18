// SPDX-License-Identifier: Apache-2.0
package com.example.retryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class MergeConfig {


    @GetMapping("/MergeConfig")
    public void mergeConfig(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = host != null ? host : "";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(synopsis.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String handshake = String.join(",", lowered);
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(handshake);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
