// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15936 {

    @PostMapping(path="/BenchmarkTest15936", consumes="text/plain")
    public void BenchmarkTest15936(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        response.setHeader("X-Forwarded-For", rawData);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
