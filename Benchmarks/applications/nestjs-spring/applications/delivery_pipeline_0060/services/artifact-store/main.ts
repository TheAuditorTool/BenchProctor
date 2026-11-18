import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PublishArtifact } from "./artifact_publish";
import { FormatApproval } from "./format_approval";
import { ArchiveBatch } from "./archive_batch";
import { PublishHeader } from "./publish_header";
import { ExportReport } from "./export_report";
import { RotateManifest } from "./rotate_manifest";
import { FormatWindow } from "./format_window";
import { PruneHeader } from "./prune_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PublishArtifact, FormatApproval, ArchiveBatch, PublishHeader, ExportReport, RotateManifest, FormatWindow, PruneHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
