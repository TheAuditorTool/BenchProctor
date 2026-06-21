// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00504 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest00504")
    public void BenchmarkTest00504(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = normalize(originValue);
        String[] values = data.split(",");
        if (values.length > 0) {
            response.setHeader("X-Param-First", values[0]);
            response.setHeader("X-Param-Dropped", String.valueOf(values.length - 1));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
