// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest29922 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/BenchmarkTest29922")
    public void BenchmarkTest29922(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(jsonValue, "form");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        response.getWriter().print("<div>" + data + "</div>");
    }
}
