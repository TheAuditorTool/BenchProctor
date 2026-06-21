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
public class BenchmarkTest55358 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @GET
    @Path("/BenchmarkTest55358")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest55358(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        FormData payload = new FormData(secretValue);
        String data = payload.payload;
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, data).compact();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
