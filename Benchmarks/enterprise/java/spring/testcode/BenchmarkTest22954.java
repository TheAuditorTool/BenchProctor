// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22954 {

    @GetMapping("/BenchmarkTest22954")
    public void BenchmarkTest22954(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = String.format("payload=%s", authHeader);
        request.isUserInRole("ADMIN");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
