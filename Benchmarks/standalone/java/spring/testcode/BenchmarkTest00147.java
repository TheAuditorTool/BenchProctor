// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00147 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping("/BenchmarkTest00147")
    public void BenchmarkTest00147(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : jsonValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        java.util.Random rng = new java.util.Random();
        int randValue = rng.nextInt() ^ data.hashCode();
        response.setHeader("X-Rand", String.valueOf(randValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
