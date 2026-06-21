// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.attribute.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73914 {

    @GetMapping("/BenchmarkTest73914")
    public void BenchmarkTest73914(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String prefix = cookieValue.length() > 0 ? cookieValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = cookieValue.toLowerCase(); break;
            case "f": data = cookieValue.toUpperCase(); break;
            default: data = cookieValue.strip(); break;
        }
        String[] modeChoices = {"rwxrwxrwx", "rwxr-xr-x", "rw-rw-rw-", "rwxrwx---", "rw-r--r--", "rwxr-x---", "r--r--r--", "rwx------"};
        String modeStr = data.matches("^[rwx-]{9}$") ? data : modeChoices[Math.abs(data.hashCode()) % modeChoices.length];
        java.util.Set<java.nio.file.attribute.PosixFilePermission> perms = java.nio.file.attribute.PosixFilePermissions.fromString(modeStr);
        java.nio.file.Files.setPosixFilePermissions(java.nio.file.Paths.get("/var/app/secret"), perms);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
