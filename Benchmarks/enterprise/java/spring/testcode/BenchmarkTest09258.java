// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09258 {

    @PostMapping(path="/BenchmarkTest09258", consumes="text/plain")
    public void BenchmarkTest09258(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        com.fasterxml.jackson.databind.JsonNode root = new com.fasterxml.jackson.databind.ObjectMapper().readTree(rawData);
        String data = root.path("value").asText();
        new java.io.File(data).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
