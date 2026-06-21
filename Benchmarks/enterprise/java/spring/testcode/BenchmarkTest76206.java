// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest76206 {

    @GetMapping("/BenchmarkTest76206/{pathId}")
    public void BenchmarkTest76206(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Set<String> allowed = java.util.Set.of("libapp", "libutils");
        if (!allowed.contains(pathValue)) { response.sendError(403); return; }
        String checkedPath = pathValue;
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
