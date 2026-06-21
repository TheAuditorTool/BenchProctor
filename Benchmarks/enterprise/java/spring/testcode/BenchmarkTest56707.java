// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest56707 {

    @GetMapping("/BenchmarkTest56707")
    public void BenchmarkTest56707(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        if (!originValue.isEmpty()) throw new IllegalArgumentException("invalid input: " + originValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
