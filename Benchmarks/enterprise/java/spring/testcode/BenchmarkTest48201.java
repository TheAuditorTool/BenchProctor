// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest48201 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/BenchmarkTest48201")
    public void BenchmarkTest48201(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(jsonValue, "json");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        response.sendError(500, data);
    }
}
