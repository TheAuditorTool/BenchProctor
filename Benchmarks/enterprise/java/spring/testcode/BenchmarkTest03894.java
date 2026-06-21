// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03894 {

    @GetMapping("/BenchmarkTest03894")
    public void BenchmarkTest03894(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.List<String> tokens = java.util.Arrays.asList(uaValue.split(","));
        String data = String.join(",", tokens);
        String[] values = data.split(",");
        if (values.length > 0) {
            response.setHeader("X-Param-First", values[0]);
            response.setHeader("X-Param-Dropped", String.valueOf(values.length - 1));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
