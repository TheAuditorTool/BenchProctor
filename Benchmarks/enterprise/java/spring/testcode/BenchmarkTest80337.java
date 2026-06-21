// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80337 {

    @GetMapping("/BenchmarkTest80337")
    public void BenchmarkTest80337(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        try {
            Integer.parseInt(originValue);
        } catch (NumberFormatException e) {
            response.sendError(400, e.getMessage()); return;
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
