// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22083 {

    @GetMapping("/BenchmarkTest22083")
    public void BenchmarkTest22083(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = authHeader.isEmpty() ? "default" : authHeader;
        new java.io.File(data).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
