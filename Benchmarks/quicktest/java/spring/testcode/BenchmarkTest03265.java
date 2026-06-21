// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03265 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/BenchmarkTest03265")
    public void BenchmarkTest03265(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{jsonValue});
        java.nio.file.Path resolvedBase = java.nio.file.Paths.get("/var/app/data").toAbsolutePath();
        java.nio.file.Path requested = resolvedBase.resolve(data).normalize();
        if (!requested.startsWith(resolvedBase)) { response.sendError(403, "outside safe scope"); return; }
        Runtime.getRuntime().exec(new String[]{"chown", "appuser:appgroup", requested.toString()}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
    }
}
