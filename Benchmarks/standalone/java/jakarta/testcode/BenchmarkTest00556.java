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
public class BenchmarkTest00556 {

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
    @Path("/BenchmarkTest00556")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00556(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data;
        try { data = new String(java.util.Base64.getDecoder().decode(authHeader), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { data = authHeader; }
        String processed = data.matches("^(noop|identity|passthrough|echo)$") ? data : "noop";
        Object codeResult = new jakarta.el.ELProcessor().eval(processed);
        response.setHeader("X-Code-Result", String.valueOf(codeResult));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
