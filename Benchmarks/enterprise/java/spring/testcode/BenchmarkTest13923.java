// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13923 {

    @GetMapping("/BenchmarkTest13923")
    public void BenchmarkTest13923(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(authHeader);
        String data = envelope.toString();
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
