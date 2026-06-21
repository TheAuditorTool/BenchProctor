// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63966 {

    @PostMapping(path="/BenchmarkTest63966", consumes="application/xml")
    public void BenchmarkTest63966(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(xmlValue);
        String data = normalizer.apply(xmlValue);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            com.fasterxml.jackson.databind.ObjectMapper unsafeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
            unsafeMapper.activateDefaultTyping(com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator.builder().allowIfBaseType(Object.class).build(), com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping.NON_FINAL);
            Object polymorphicObj = unsafeMapper.readValue(data, Object.class);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
