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
public class BenchmarkTest00404 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

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
    @Path("/BenchmarkTest00404/graphql")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00404(GraphQLRequest req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String data;
        try { data = String.valueOf(Integer.parseInt(graphqlVar)); }
        catch (NumberFormatException e) { data = graphqlVar; }
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("DESede/CBC/PKCS5Padding");
        byte[] desedeIv = new byte[8]; new java.security.SecureRandom().nextBytes(desedeIv);
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, new javax.crypto.spec.SecretKeySpec(java.util.Base64.getDecoder().decode(java.util.Objects.requireNonNullElse(System.getenv("LEGACY_DESEDE_KEY"), "")), "DESede"), new javax.crypto.spec.IvParameterSpec(desedeIv));
        byte[] ct = cipher.doFinal(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
