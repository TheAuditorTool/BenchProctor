import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RunSettlement } from "./settlement_batch";
import { FetchBundle } from "./fetch_bundle";
import { ArchiveCheckpoint } from "./archive_checkpoint";
import { ValidateStatement } from "./validate_statement";
import { SummarizeReport } from "./summarize_report";
import { MergeConfig } from "./merge_config";
import { ArchiveSchedule } from "./archive_schedule";
import { SummarizeHeader } from "./summarize_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RunSettlement, FetchBundle, ArchiveCheckpoint, ValidateStatement, SummarizeReport, MergeConfig, ArchiveSchedule, SummarizeHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
