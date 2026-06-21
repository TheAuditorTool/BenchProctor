// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest47149 {

    @GetMapping("/BenchmarkTest47149")
    public void BenchmarkTest47149(HttpServletRequest request, HttpServletResponse response) throws Exception {
        if (!request.isUserInRole("ADMIN")) {
            response.sendError(403, "forbidden"); return;
        }
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
