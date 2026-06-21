// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20161 {

    @GetMapping("/BenchmarkTest20161")
    public void BenchmarkTest20161(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = String.format("%s", hostValue);
        response.sendRedirect(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
