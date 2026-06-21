// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest42914 {

    @GetMapping("/BenchmarkTest42914")
    public void BenchmarkTest42914(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        byte[] buf = new byte[Integer.parseInt(originValue)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
