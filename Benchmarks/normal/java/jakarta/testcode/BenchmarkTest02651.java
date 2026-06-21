// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest02651 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GET
    @Path("/BenchmarkTest02651/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02651(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = stripCRLF(pathValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        return Response.ok(processed + ",data\n", "text/csv").build();
    }
}
