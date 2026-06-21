// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest28293 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @GetMapping("/BenchmarkTest28293/{pathId}")
    public void BenchmarkTest28293(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = collapseWhitespace(pathValue);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            java.nio.file.Files.write(java.nio.file.Paths.get("plugins/generated.js"), ("var setting = '" + data + "';").getBytes());
            javax.script.ScriptEngine engine = new javax.script.ScriptEngineManager().getEngineByName("nashorn");
            engine.eval(new java.io.FileReader("plugins/generated.js"));
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
