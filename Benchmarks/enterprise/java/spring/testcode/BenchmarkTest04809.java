// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04809 {

    @PostMapping("/BenchmarkTest04809")
    public void BenchmarkTest04809(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        response.addCookie(new Cookie("session", fieldValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
