// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest25404 {

    @GetMapping("/BenchmarkTest25404")
    public void BenchmarkTest25404(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String prefix = cookieValue.length() > 0 ? cookieValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = cookieValue.toLowerCase(); break;
            case "f": data = cookieValue.toUpperCase(); break;
            default: data = cookieValue.strip(); break;
        }
        String content = Files.readString(Paths.get("/var/app/data/" + data), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
