// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest41424 {

    @GetMapping("/BenchmarkTest41424")
    public void BenchmarkTest41424(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String configValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.json")))).orElse("");
        String prefix = configValue.length() > 0 ? configValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = configValue.toLowerCase(); break;
            case "f": data = configValue.toUpperCase(); break;
            default: data = configValue.strip(); break;
        }
        Cookie cookie = new Cookie("session", data);
        cookie.setMaxAge(86400);
        response.addCookie(cookie);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
