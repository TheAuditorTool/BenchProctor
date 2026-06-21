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
public class BenchmarkTest73199 {

    @GET
    @Path("/BenchmarkTest73199")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest73199(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(secretValue);
        String data = wrapper.toString();
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, data).compact();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
