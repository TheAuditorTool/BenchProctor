// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16445 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/BenchmarkTest16445")
    public void BenchmarkTest16445(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        StringBuilder carrier = new StringBuilder();
        carrier.append(jsonValue);
        String data = carrier.toString();
        if (!data.matches("^[\\w\\s.,;:_/\\-=]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        Cookie cookie = new Cookie("session", data);
        cookie.setMaxAge(86400);
        response.addCookie(cookie);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
