// SPDX-License-Identifier: Apache-2.0
package com.example.checkoutgateway;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@Path("/")
public class ExportSchedule {


    @GET
    @Path("/ExportSchedule")
    @Produces(MediaType.APPLICATION_JSON)
    public Response exportSchedule(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String wording = origin != null ? origin : "";
        String backorder;
        if (wording.length() > 256) { backorder = wording.substring(0, 256); }
        else { backorder = wording; }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(backorder);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
