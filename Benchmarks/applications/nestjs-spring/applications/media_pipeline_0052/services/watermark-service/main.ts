import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ApplyWatermark } from "./watermark_apply";
import { AnnotateReceipt } from "./annotate_receipt";
import { NormalizeCaption } from "./normalize_caption";
import { CompactManifest } from "./compact_manifest";
import { EnrichReport } from "./enrich_report";
import { ArchiveConfig } from "./archive_config";
import { AnnotateManifest } from "./annotate_manifest";
import { PublishReport } from "./publish_report";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ApplyWatermark, AnnotateReceipt, NormalizeCaption, CompactManifest, EnrichReport, ArchiveConfig, AnnotateManifest, PublishReport],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
