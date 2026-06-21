// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest07455 {

    @GetMapping("/BenchmarkTest07455")
    public void BenchmarkTest07455(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        if (!request.isUserInRole("ADMIN")) {
            response.sendError(403, "forbidden"); return;
        }
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
