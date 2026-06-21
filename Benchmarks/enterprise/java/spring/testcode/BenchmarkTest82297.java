// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest82297 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @GetMapping("/BenchmarkTest82297")
    public void BenchmarkTest82297(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        FormData payload = new FormData(originValue);
        String data = payload.payload;
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException e) {
            response.sendError(400, e.getMessage()); return;
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
