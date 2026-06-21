// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest56364 {

    @GET
    @Path("/BenchmarkTest56364")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest56364(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = uaValue.isEmpty() ? "default" : uaValue;
        String escaped = "\"" + data.replace("\"", "\"\"") + "\"";
        return Response.ok(escaped + ",data", "text/csv").build();
    }
}
