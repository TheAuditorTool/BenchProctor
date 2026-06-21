// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest45200 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest45200/{pathId}")
    public void BenchmarkTest45200(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        stateBox.set(pathValue);
        String data = stateBox.get();
        Integer.parseInt(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
