// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest30336 {

    @PostMapping(path="/BenchmarkTest30336", consumes="text/plain")
    public void BenchmarkTest30336(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String[] values = rawData.split(",");
        if (values.length > 0) {
            response.setHeader("X-Param-First", values[0]);
            response.setHeader("X-Param-Dropped", String.valueOf(values.length - 1));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
