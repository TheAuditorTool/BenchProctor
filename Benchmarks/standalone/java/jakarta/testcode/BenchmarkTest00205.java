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
public class BenchmarkTest00205 {

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

    @POST
    @Path("/BenchmarkTest00205")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00205(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = rawData.replace("\u0000", "");
        if (!data.matches("^[a-zA-Z0-9 _.\\-]+$")) { return Response.status(400).build(); }
        java.util.Map<String, Object> sessionProfile = (java.util.Map<String, Object>) request.getSession().getAttribute("profile");
        if (sessionProfile == null) {
            sessionProfile = new java.util.concurrent.ConcurrentHashMap<>();
            request.getSession().setAttribute("profile", sessionProfile);
        }
        sessionProfile.putAll(java.util.Map.of("displayName", data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
