// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02526 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/BenchmarkTest02526")
    public void BenchmarkTest02526(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        if (!jsonValue.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        request.setAttribute("hidden_form_field", jsonValue);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
