// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest34140 {

    @GetMapping("/BenchmarkTest34140/{pathId}")
    public void BenchmarkTest34140(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        StringBuilder carrier = new StringBuilder();
        carrier.append(pathValue);
        String data = carrier.toString();
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + data}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
