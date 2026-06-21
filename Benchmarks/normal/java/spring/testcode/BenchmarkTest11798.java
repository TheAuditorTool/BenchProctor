// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest11798 {

    @PostMapping(path="/BenchmarkTest11798", consumes="text/plain")
    public void BenchmarkTest11798(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        if ("https://app.acmecdn.net".equals(rawData)) response.setHeader("Access-Control-Allow-Origin", rawData);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
