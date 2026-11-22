// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.validation.Valid;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00248 {
    private static class UserInput {
        @javax.validation.constraints.NotNull
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

    @PostMapping("/BenchmarkTest00248")
    public void BenchmarkTest00248(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        com.fasterxml.jackson.databind.JsonNode root = new com.fasterxml.jackson.databind.ObjectMapper().readTree(jsonValue);
        String data = root.path("value").asText();
        int recordCount = Integer.parseInt(data);
        java.nio.ByteBuffer exportBuffer = java.nio.ByteBuffer.allocate(recordCount * 512);
        response.setHeader("X-Export-Capacity", String.valueOf(exportBuffer.capacity()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
