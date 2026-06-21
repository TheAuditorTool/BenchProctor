// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest47124 {

    @GET
    @Path("/BenchmarkTest47124/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest47124(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        return Response.ok(pathValue + ",data\n", "text/csv").build();
    }
}
