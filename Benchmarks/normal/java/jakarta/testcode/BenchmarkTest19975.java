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
public class BenchmarkTest19975 {

    @GET
    @Path("/BenchmarkTest19975")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest19975(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "default_config_label";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(secretValue, "request");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
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
