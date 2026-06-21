// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest59625 {

    @GetMapping("/BenchmarkTest59625")
    public void BenchmarkTest59625(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(uaValue);
        String data = carrier.toString();
        response.sendError(500, data);
    }
}
