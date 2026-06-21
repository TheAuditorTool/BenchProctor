// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06415 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest06415")
    public void BenchmarkTest06415(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = normalize(originValue);
        Integer.parseInt(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
