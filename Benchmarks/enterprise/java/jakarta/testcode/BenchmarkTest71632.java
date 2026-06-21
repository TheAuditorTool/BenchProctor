// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest71632 {

    @GET
    @Path("/BenchmarkTest71632/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest71632(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = pathValue.isEmpty() ? "default" : pathValue;
        new java.io.File("/tmp/" + data).createNewFile();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
