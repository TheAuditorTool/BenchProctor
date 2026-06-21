// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest59505 {

    @GET
    @Path("/BenchmarkTest59505/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest59505(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(pathValue.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String data = String.join(",", lowered);
        return Response.ok(data + ",data\n", "text/csv").build();
    }
}
