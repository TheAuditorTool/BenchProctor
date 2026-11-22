import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { SchedulePublication } from "./publish_schedule";
import { ResolveSchedule } from "./resolve_schedule";
import { NormalizeCheckpoint } from "./normalize_checkpoint";
import { SummarizeSummary } from "./summarize_summary";
import { SummarizeRevision } from "./summarize_revision";
import { EnrichSchedule } from "./enrich_schedule";
import { MergeRevision } from "./merge_revision";
import { FormatIndex } from "./format_index";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SchedulePublication, ResolveSchedule, NormalizeCheckpoint, SummarizeSummary, SummarizeRevision, EnrichSchedule, MergeRevision, FormatIndex],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
