// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest31487 {

    @PostMapping(path="/BenchmarkTest31487", consumes="text/plain")
    public void BenchmarkTest31487(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.nio.file.Files.write(java.nio.file.Paths.get("plugins/generated.js"), ("var setting = '" + rawData + "';").getBytes());
        javax.script.ScriptEngine engine = new javax.script.ScriptEngineManager().getEngineByName("nashorn");
        engine.eval(new java.io.FileReader("plugins/generated.js"));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
