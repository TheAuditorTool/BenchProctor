// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest32004 {

    @GetMapping("/BenchmarkTest32004")
    public void BenchmarkTest32004(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = String.format("%s", originValue);
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException nfe) {
            response.sendError(400, "invalid number"); return;
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
