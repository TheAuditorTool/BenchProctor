// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest67329 {

    @GET
    @Path("/BenchmarkTest67329")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest67329(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = String.join(" ", userId.split("\\s+"));
        String reflectStatus = "ok";
        try {
            Class<?> reflectCls = Class.forName(data);
            java.lang.reflect.Method reflectMethod = reflectCls.getDeclaredMethod("toString");
            Object invokeResult = reflectMethod.invoke(reflectCls.getDeclaredConstructor().newInstance());
            response.setHeader("X-Reflect-Result", String.valueOf(invokeResult));
        } catch (ReflectiveOperationException re) { reflectStatus = "class-not-found"; }
        response.setHeader("X-Reflect-Status", reflectStatus);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
