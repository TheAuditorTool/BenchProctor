// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest65107 {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest65107")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest65107(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        valueRef.set(refererValue);
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
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
