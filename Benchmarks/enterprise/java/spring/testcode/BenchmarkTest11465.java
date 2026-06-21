// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest11465 {

    @GetMapping("/BenchmarkTest11465")
    public void BenchmarkTest11465(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        new java.io.File(forwardedIp).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
