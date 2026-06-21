// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest25856 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping("/BenchmarkTest25856")
    public void BenchmarkTest25856(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        stateBox.set(commentValue);
        String data = stateBox.get();
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            response.getWriter().print("<div>" + data + "</div>");
        }
    }
}
