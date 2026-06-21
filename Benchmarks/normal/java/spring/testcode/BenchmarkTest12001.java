// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12001 {

    @PostMapping(path="/BenchmarkTest12001", consumes="text/plain")
    public void BenchmarkTest12001(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        if (!("true".equals(rawData) || "false".equals(rawData))) { response.sendError(400); return; }
        response.setHeader("X-Forwarded-For", rawData);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
