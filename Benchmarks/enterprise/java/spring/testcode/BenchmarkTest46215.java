// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest46215 {

    @GetMapping("/BenchmarkTest46215")
    public void BenchmarkTest46215(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        int result = 100 / Integer.parseInt(originValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
