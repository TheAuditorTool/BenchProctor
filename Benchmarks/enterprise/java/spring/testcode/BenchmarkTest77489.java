// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest77489 {

    @GetMapping("/BenchmarkTest77489")
    public void BenchmarkTest77489(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.function.Function<String, String> initialFn = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::trim);
        String data = transformed.apply(originValue);
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
