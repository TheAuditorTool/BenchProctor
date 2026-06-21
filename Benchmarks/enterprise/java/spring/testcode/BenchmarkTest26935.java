// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest26935 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping(path="/BenchmarkTest26935", consumes="application/json")
    public void BenchmarkTest26935(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        valueRef.set(graphqlVar);
        String data = valueRef.get();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            String reflectStatus = "ok";
            try {
                Class<?> reflectCls = Class.forName(data);
                java.lang.reflect.Method reflectMethod = reflectCls.getDeclaredMethod("toString");
                Object invokeResult = reflectMethod.invoke(reflectCls.getDeclaredConstructor().newInstance());
                response.setHeader("X-Reflect-Result", String.valueOf(invokeResult));
            } catch (ReflectiveOperationException re) { reflectStatus = "class-not-found"; }
            response.setHeader("X-Reflect-Status", reflectStatus);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
