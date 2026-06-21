// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest09588 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest09588")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09588(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = normalize(authHeader);
        return Response.ok(data + ",data\n", "text/csv").build();
    }
}
