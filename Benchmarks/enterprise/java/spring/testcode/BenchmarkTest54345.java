// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest54345 {

    @PostMapping("/BenchmarkTest54345")
    public void BenchmarkTest54345(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        StringBuilder carrier = new StringBuilder();
        carrier.append(commentValue);
        String data = carrier.toString();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            com.fasterxml.jackson.databind.ObjectMapper unsafeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
            unsafeMapper.activateDefaultTyping(com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator.builder().allowIfBaseType(Object.class).build(), com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping.NON_FINAL);
            Object polymorphicObj = unsafeMapper.readValue(data, Object.class);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
