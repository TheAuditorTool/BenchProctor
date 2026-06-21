// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest26720 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest26720")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest26720(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = normalize(refererValue);
        return Response.ok(data + ",data\n", "text/csv").build();
    }
}
