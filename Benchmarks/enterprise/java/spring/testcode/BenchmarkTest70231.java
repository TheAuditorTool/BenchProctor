// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest70231 {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest70231")
    public void BenchmarkTest70231(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        valueRef.set(envValue);
        String data = valueRef.get();
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            java.nio.file.Files.write(java.nio.file.Paths.get("plugins/generated.js"), ("var setting = '" + data + "';").getBytes());
            javax.script.ScriptEngine engine = new javax.script.ScriptEngineManager().getEngineByName("nashorn");
            engine.eval(new java.io.FileReader("plugins/generated.js"));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
