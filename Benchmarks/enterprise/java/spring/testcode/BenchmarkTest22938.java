// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22938 {

    @GetMapping("/BenchmarkTest22938")
    public void BenchmarkTest22938(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = String.format("payload=%s", originValue);
        java.util.Set<String> allowed = java.util.Set.of("libapp", "libutils");
        if (!allowed.contains(data)) { response.sendError(403); return; }
        String checkedPath = data;
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
