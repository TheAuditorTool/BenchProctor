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
public class BenchmarkTest00206 {

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
    @Path("/BenchmarkTest00206")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00206(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = String.format("%s", authHeader);
        java.util.Map<String, String> regionEndpoints = java.util.Map.of("us-east", "https://us-east.api.svc.local", "eu-west", "https://eu-west.api.svc.local");
        String regionEndpoint = regionEndpoints.get(data);
        if (regionEndpoint == null) { return Response.status(404).entity("unknown region").build(); }
        boolean secureEndpoint = regionEndpoint.startsWith("https://");
        response.setHeader("X-Region-Secure", String.valueOf(secureEndpoint));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
