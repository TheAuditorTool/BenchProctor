// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest19814 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest19814")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest19814(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data = normalize(cookieValue);
        return Response.ok(data + ",data\n", "text/csv").build();
    }
}
