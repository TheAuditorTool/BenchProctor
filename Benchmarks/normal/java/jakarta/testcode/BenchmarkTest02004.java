// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest02004 {

    @GET
    @Path("/BenchmarkTest02004")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02004(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String prefix = userId.length() > 0 ? userId.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = userId.toLowerCase(); break;
            case "f": data = userId.toUpperCase(); break;
            default: data = userId.strip(); break;
        }
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(data);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
