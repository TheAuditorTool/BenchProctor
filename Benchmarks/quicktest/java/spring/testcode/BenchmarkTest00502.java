// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00502 {

    @PostMapping(path="/BenchmarkTest00502", consumes="application/xml")
    public void BenchmarkTest00502(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        byte[] raw = xmlValue.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String data = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        java.nio.file.Files.write(java.nio.file.Paths.get("plugins/generated.js"), ("var setting = '" + data + "';").getBytes());
        javax.script.ScriptEngine engine = new javax.script.ScriptEngineManager().getEngineByName("nashorn");
        engine.eval(new java.io.FileReader("plugins/generated.js"));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
