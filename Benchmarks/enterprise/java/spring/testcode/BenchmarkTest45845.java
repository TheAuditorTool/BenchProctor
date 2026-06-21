// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest45845 {

    @PostMapping(path="/BenchmarkTest45845", consumes="multipart/form-data")
    public void BenchmarkTest45845(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        response.addCookie(new Cookie("session", multipartValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
