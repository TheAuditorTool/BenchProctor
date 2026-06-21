// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest54658 {

    @GET
    @Path("/BenchmarkTest54658")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest54658(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(userId);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
