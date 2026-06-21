// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12411 {

    @PostMapping(path="/BenchmarkTest12411", consumes="text/plain")
    public void BenchmarkTest12411(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        com.fasterxml.jackson.databind.JsonNode root = new com.fasterxml.jackson.databind.ObjectMapper().readTree(rawData);
        String data = root.path("value").asText();
        if (!new java.io.File("/var/app/data", new java.io.File(data).getName()).delete()) { response.sendError(500, "delete failed"); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
