// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest66902 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @POST
    @Path("/BenchmarkTest66902")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest66902(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = expandTabs(fieldValue);
        javax.crypto.Mac authMac = javax.crypto.Mac.getInstance("HmacSHA256");
        authMac.init(new javax.crypto.spec.SecretKeySpec(System.getenv("HMAC_SECRET").getBytes(java.nio.charset.StandardCharsets.UTF_8), "HmacSHA256"));
        byte[] presented = authMac.doFinal(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        byte[] stored = java.util.Base64.getDecoder().decode((String) request.getSession().getAttribute("credHash"));
        if (!java.security.MessageDigest.isEqual(presented, stored)) { return Response.status(401).build(); }
        return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
    }
}
