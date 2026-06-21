// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03987 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @GetMapping("/BenchmarkTest03987")
    public void BenchmarkTest03987(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        FormData payload = new FormData(userId);
        String data = payload.payload;
        response.addCookie(new Cookie("session", data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
