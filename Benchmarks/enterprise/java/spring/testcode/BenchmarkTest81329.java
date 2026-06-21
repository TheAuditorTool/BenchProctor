// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81329 {

    @PostMapping(path="/BenchmarkTest81329", consumes="text/plain")
    public void BenchmarkTest81329(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        com.fasterxml.jackson.databind.JsonNode root = new com.fasterxml.jackson.databind.ObjectMapper().readTree(rawData);
        String data = root.path("value").asText();
        String processed = org.owasp.encoder.Encode.forHtml(data);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
