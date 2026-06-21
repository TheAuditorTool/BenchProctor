// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00970 {

    @GetMapping("/BenchmarkTest00970")
    public void BenchmarkTest00970(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        if (!new java.io.File("/var/app/data", new java.io.File(envValue).getName()).delete()) { response.sendError(500, "delete failed"); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
