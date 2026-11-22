// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.glassfish.jersey.media.multipart.FormDataParam;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00022 {

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
    @Path("/BenchmarkTest00022")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00022(@jakarta.validation.constraints.Size(max = 4096) @FormDataParam("multipart_field") String multipartField, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(multipartValue.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String data = String.join(",", lowered);
        byte[] dataKey = java.util.Base64.getDecoder().decode(System.getenv("DATA_ENC_KEY"));
        byte[] gcmNonce = new byte[12]; new java.security.SecureRandom().nextBytes(gcmNonce);
        org.bouncycastle.crypto.modes.GCMModeCipher blockMode = org.bouncycastle.crypto.modes.GCMBlockCipher.newInstance(org.bouncycastle.crypto.engines.AESEngine.newInstance());
        blockMode.init(true, new org.bouncycastle.crypto.params.AEADParameters(new org.bouncycastle.crypto.params.KeyParameter(dataKey), 128, gcmNonce));
        byte[] plain = data.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        byte[] sealed = new byte[blockMode.getOutputSize(plain.length)];
        int sealedLen = blockMode.processBytes(plain, 0, plain.length, sealed, 0);
        sealedLen += blockMode.doFinal(sealed, sealedLen);
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(java.util.Arrays.copyOf(sealed, sealedLen)));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
