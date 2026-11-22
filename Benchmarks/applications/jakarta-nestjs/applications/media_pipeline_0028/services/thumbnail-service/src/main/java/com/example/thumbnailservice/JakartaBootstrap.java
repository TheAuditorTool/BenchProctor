package com.example.thumbnailservice;

public class JakartaBootstrap {

    @jakarta.ws.rs.Path("/health")
    public static class HealthResource {
        @jakarta.ws.rs.GET
        public jakarta.ws.rs.core.Response health() {
            return jakarta.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.thumbnailservice.JakartaBootstrap$HealthResource,com.example.thumbnailservice.CollectPolicy,com.example.thumbnailservice.CollectRecord,com.example.thumbnailservice.MergeReceipt,com.example.thumbnailservice.NormalizeReceipt,com.example.thumbnailservice.PruneCheckpoint,com.example.thumbnailservice.RenderAsset,com.example.thumbnailservice.RenderThumbnail,com.example.thumbnailservice.ResolvePolicy,org.glassfish.jersey.media.multipart.MultiPartFeature");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
