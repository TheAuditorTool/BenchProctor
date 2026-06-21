// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest58940 {

    @GetMapping("/BenchmarkTest58940")
    public void BenchmarkTest58940(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = "" + authHeader;
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException e) {
            response.sendError(400, e.getMessage()); return;
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
