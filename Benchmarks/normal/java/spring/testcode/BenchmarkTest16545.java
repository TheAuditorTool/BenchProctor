// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16545 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest16545")
    public void BenchmarkTest16545(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = normalize(originValue);
        response.setHeader("Refresh", "0; url=" + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
