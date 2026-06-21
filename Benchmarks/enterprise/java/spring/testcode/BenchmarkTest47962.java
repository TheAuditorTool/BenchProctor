// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest47962 {

    @GetMapping("/BenchmarkTest47962")
    public void BenchmarkTest47962(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = String.join(" ", originValue.split("\\s+"));
        com.fasterxml.jackson.databind.ObjectMapper unsafeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        unsafeMapper.activateDefaultTyping(com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator.builder().allowIfBaseType(Object.class).build(), com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping.NON_FINAL);
        Object polymorphicObj = unsafeMapper.readValue(data, Object.class);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
