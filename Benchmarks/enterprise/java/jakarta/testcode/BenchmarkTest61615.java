// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest61615 {

    @GET
    @Path("/BenchmarkTest61615")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest61615(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> authHeader)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        if (System.currentTimeMillis() > 1000000000000L) {
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
