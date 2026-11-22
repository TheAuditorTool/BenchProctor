// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.container.ContainerRequestContext;
import javax.ws.rs.container.ContainerRequestFilter;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00065 {

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

    static final class FormData {
        private final String payload;
        FormData(String payload) { this.payload = payload; }
        String getPayload() { return payload; }
    }

    @GET
    @Path("/BenchmarkTest00065")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00065(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        FormData payload = new FormData(originValue);
        String data = payload.getPayload();
        byte[] dataKey = java.util.Base64.getDecoder().decode(System.getenv("DATA_ENC_KEY"));
        byte[] streamNonce = new byte[12]; new java.security.SecureRandom().nextBytes(streamNonce);
        org.bouncycastle.crypto.modes.ChaCha20Poly1305 aead = new org.bouncycastle.crypto.modes.ChaCha20Poly1305();
        aead.init(true, new org.bouncycastle.crypto.params.ParametersWithIV(new org.bouncycastle.crypto.params.KeyParameter(dataKey), streamNonce));
        byte[] plain = data.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        byte[] sealed = new byte[aead.getOutputSize(plain.length)];
        int sealedLen = aead.processBytes(plain, 0, plain.length, sealed, 0);
        aead.doFinal(sealed, sealedLen);
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(sealed));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
