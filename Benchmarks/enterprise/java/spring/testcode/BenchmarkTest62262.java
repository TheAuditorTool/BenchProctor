// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest62262 {

    @GetMapping("/BenchmarkTest62262")
    public void BenchmarkTest62262(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(uaValue);
        String data = bundle.toString();
        response.sendError(500, data);
    }
}
