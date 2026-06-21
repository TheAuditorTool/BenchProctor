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
public class BenchmarkTest00185 {

    @GET
    @Path("/BenchmarkTest00185")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00185(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "s3cr3t_key_test_xyz";
        String data;
        if (secretValue.length() > 256) { data = secretValue.substring(0, 256); }
        else { data = secretValue; }
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, data).compact();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
