// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00617 {

    @Provider
    public static class BindingRestrictionFilter implements ContainerRequestFilter {
        @Override
        public void filter(ContainerRequestContext requestContext) {
            requestContext.getHeaders().remove("X-Internal-Bind");
        }
    }

    @Provider
    public static class FailureMapper implements ExceptionMapper<Exception> {
        @Override
        public Response toResponse(Exception ex) {
            return Response.status(500).entity("request failed").build();
        }
    }

    @GET
    @Path("/BenchmarkTest00617")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00617(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(originValue, "json");
        String data = entry.getKey();
        if (!("true".equals(data) || "false".equals(data))) { return Response.status(400).build(); }
        String validatedName = data.matches("[A-Za-z][A-Za-z .'-]{0,63}") ? data.strip() : "guest";
        request.getSession().setAttribute("displayName", validatedName);
        String greetingName = String.valueOf(request.getSession().getAttribute("displayName"));
        return Response.ok("{\"greetingLength\":" + greetingName.length() + "}", MediaType.APPLICATION_JSON).build();
    }
}
