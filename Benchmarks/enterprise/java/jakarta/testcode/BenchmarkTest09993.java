// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09993 {

    @GET
    @Path("/BenchmarkTest09993")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09993(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(userId);
        String data = envelope.toString();
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
