// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest04604 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest04604")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04604(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = normalize(hostValue);
        String escaped = "\"" + data.replace("\"", "\"\"") + "\"";
        return Response.ok(escaped + ",data", "text/csv").build();
    }
}
