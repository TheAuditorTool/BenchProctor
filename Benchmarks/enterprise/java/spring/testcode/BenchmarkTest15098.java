// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15098 {

    @GetMapping("/BenchmarkTest15098")
    public void BenchmarkTest15098(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(refererValue).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String checkedPath = resolved.toString();
        String libName = java.nio.file.Paths.get(checkedPath).getFileName().toString();
        java.util.Set<String> allowedLibs = java.util.Set.of("libapp", "libutils");
        if (!allowedLibs.contains(libName)) {
            response.sendError(403, "library not allowed"); return;
        }
        System.loadLibrary(libName);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
