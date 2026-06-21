// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03242 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest03242")
    public void BenchmarkTest03242(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = normalize(originValue);
        int requested = Integer.parseInt(data);
        int allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
