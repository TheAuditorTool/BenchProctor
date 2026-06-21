// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest30468 {

    @GetMapping("/BenchmarkTest30468")
    public void BenchmarkTest30468(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = "" + forwardedIp;
        new java.io.File(data).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
