// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36814 {

    @PostMapping(path="/BenchmarkTest36814", consumes="application/xml")
    public void BenchmarkTest36814(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        if (!request.isUserInRole("ADMIN")) {
            response.sendError(403, "forbidden"); return;
        }
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
