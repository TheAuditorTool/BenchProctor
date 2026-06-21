// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest77614 {

    @GetMapping("/BenchmarkTest77614")
    public void BenchmarkTest77614(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(forwardedIp);
        String data = wrapper.toString();
        response.sendError(500, data);
    }
}
