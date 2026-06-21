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
public class BenchmarkTest68019 {

    private static final java.util.concurrent.atomic.AtomicReference<String> sharedRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest68019")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest68019(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "default_config_label";
        sharedRef.set(secretValue);
        String data = sharedRef.get();
        if (data == null) throw new IllegalArgumentException("input required");
        java.util.Properties props = new java.util.Properties();
        try (java.io.InputStream propsStream = new java.io.FileInputStream("/etc/app/credentials.properties")) {
            props.load(propsStream);
        }
        String storeCred = props.getProperty("api.key", "");
        String secret = storeCred;
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, secret).compact();
        return Response.ok("{\"signed\":\"ok\"}", MediaType.APPLICATION_JSON).build();
    }
}
