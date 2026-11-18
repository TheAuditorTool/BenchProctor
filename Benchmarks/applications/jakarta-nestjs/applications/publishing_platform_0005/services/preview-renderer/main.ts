import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RenderPreview } from "./preview_render";
import { AnnotateSummary } from "./annotate_summary";
import { PruneThreshold } from "./prune_threshold";
import { FormatRevision } from "./format_revision";
import { AuditManifest } from "./audit_manifest";
import { PruneArticle } from "./prune_article";
import { PublishWindow } from "./publish_window";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RenderPreview, AnnotateSummary, PruneThreshold, FormatRevision, AuditManifest, PruneArticle, PublishWindow],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
