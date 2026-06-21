// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest54584 {

    @GetMapping("/BenchmarkTest54584")
    public void BenchmarkTest54584(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(forwardedIp)); }
        catch (NumberFormatException e) { data = forwardedIp; }
        response.sendError(500, data);
    }
}
