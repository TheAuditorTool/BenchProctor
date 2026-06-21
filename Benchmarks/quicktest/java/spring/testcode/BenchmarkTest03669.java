// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03669 {

    @GetMapping("/BenchmarkTest03669")
    public void BenchmarkTest03669(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : uaValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        response.sendError(500, data);
    }
}
