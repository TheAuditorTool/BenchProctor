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
public class BenchmarkTest44989 {

    @GET
    @Path("/BenchmarkTest44989")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest44989(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        String data = secretValue.isEmpty() ? "default" : secretValue;
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, data).compact();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
