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
public class BenchmarkTest12245 {

    @GET
    @Path("/BenchmarkTest12245")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12245(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "feature_flag_value";
        String prefix = secretValue.length() > 0 ? secretValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = secretValue.toLowerCase(); break;
            case "f": data = secretValue.toUpperCase(); break;
            default: data = secretValue.strip(); break;
        }
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
