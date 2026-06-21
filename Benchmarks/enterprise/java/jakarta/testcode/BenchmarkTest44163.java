// SPDX-License-Identifier: Apache-2.0
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest44163 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest44163")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest44163(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "default_setting_value";
        String data = normalize(secretValue);
        if (data == null) throw new IllegalArgumentException("input required");
        String envSecret = System.getenv("APP_SECRET");
        if (envSecret == null) throw new IllegalStateException("APP_SECRET unset");
        String storeCred = envSecret;
        String secret = storeCred;
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, secret).compact();
        return Response.ok("{\"signed\":\"ok\"}", MediaType.APPLICATION_JSON).build();
    }
}
