import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { IngestMetric } from "./metric_ingest";
import { AuditSchedule } from "./audit_schedule";
import { PruneBatch } from "./prune_batch";
import { ExportAlert } from "./export_alert";
import { RenderManifest } from "./render_manifest";
import { FormatSchedule } from "./format_schedule";
import { AnnotateDigest } from "./annotate_digest";
import { ExportSchedule } from "./export_schedule";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, IngestMetric, AuditSchedule, PruneBatch, ExportAlert, RenderManifest, FormatSchedule, AnnotateDigest, ExportSchedule],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
