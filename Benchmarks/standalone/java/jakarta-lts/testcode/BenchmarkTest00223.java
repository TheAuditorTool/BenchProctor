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
public class BenchmarkTest00223 {

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
    @Path("/BenchmarkTest00223")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00223(@jakarta.validation.constraints.Size(max = 4096) String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", xmlValue);
        String data = box.getProperty("value", "");
        org.bouncycastle.crypto.Digest contentDigest = new org.bouncycastle.crypto.digests.SHA256Digest();
        byte[] digestInput = data.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        contentDigest.update(digestInput, 0, digestInput.length);
        byte[] digest = new byte[contentDigest.getDigestSize()];
        contentDigest.doFinal(digest, 0);
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
