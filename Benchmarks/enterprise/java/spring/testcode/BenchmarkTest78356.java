// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest78356 {

    @GetMapping("/BenchmarkTest78356")
    public void BenchmarkTest78356(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(cookieValue);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
