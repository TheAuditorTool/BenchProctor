import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SweepRetention } from "./retention_sweep";
import { RotateCheckpoint } from "./rotate_checkpoint";
import { ValidateCheckpoint } from "./validate_checkpoint";
import { CompactBatch } from "./compact_batch";
import { ArchiveSchedule } from "./archive_schedule";
import { AnnotateHeader } from "./annotate_header";
import { CollectReport } from "./collect_report";
import { FetchThreshold } from "./fetch_threshold";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SweepRetention, RotateCheckpoint, ValidateCheckpoint, CompactBatch, ArchiveSchedule, AnnotateHeader, CollectReport, FetchThreshold],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
