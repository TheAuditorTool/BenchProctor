// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest27689 {

    @PostMapping(path="/BenchmarkTest27689", consumes="application/xml")
    public void BenchmarkTest27689(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        response.addCookie(new Cookie("session", xmlValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
