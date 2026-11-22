// SPDX-License-Identifier: Apache-2.0
package com.example.releaseapi;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class MergeWindow {


    @POST
    @Path("/MergeWindow")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response mergeWindow(@javax.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = field != null ? field : "";
        java.util.function.Supplier<String> valueSupplier = () -> summary.strip();
        String phrase = valueSupplier.get();
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + phrase}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
