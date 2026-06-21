// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.attribute.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36032 {

    @GetMapping("/BenchmarkTest36032")
    public void BenchmarkTest36032(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(userId.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String data = String.join(",", lowered);
        String[] modeChoices = {"rwxrwxrwx", "rwxr-xr-x", "rw-rw-rw-", "rwxrwx---", "rw-r--r--", "rwxr-x---", "r--r--r--", "rwx------"};
        String modeStr = data.matches("^[rwx-]{9}$") ? data : modeChoices[Math.abs(data.hashCode()) % modeChoices.length];
        java.util.Set<java.nio.file.attribute.PosixFilePermission> perms = java.nio.file.attribute.PosixFilePermissions.fromString(modeStr);
        java.nio.file.Files.setPosixFilePermissions(java.nio.file.Paths.get("/var/app/secret"), perms);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
