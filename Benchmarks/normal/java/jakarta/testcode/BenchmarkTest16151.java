// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16151 {

    @POST
    @Path("/BenchmarkTest16151")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16151(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String reflectStatus = "ok";
        try {
            Class<?> reflectCls = Class.forName(fieldValue);
            java.lang.reflect.Method reflectMethod = reflectCls.getDeclaredMethod("toString");
            Object invokeResult = reflectMethod.invoke(reflectCls.getDeclaredConstructor().newInstance());
            response.setHeader("X-Reflect-Result", String.valueOf(invokeResult));
        } catch (ReflectiveOperationException re) { reflectStatus = "class-not-found"; }
        response.setHeader("X-Reflect-Status", reflectStatus);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
