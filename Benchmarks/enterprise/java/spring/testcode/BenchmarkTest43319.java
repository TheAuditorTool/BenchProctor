// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest43319 {

    @GetMapping("/BenchmarkTest43319")
    public void BenchmarkTest43319(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        response.setHeader("Access-Control-Allow-Origin", authHeader);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
