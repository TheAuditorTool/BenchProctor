// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17210 {

    @PostMapping(path="/BenchmarkTest17210", consumes="text/plain")
    public void BenchmarkTest17210(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        response.setHeader("X-Forwarded-For", rawData);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
