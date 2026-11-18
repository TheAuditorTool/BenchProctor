import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PostLedgerEntry } from "./ledger_post";
import { ValidateHeader } from "./validate_header";
import { ArchiveIndex } from "./archive_index";
import { ValidateSummary } from "./validate_summary";
import { LoadRoster } from "./load_roster";
import { ExportDunning } from "./export_dunning";
import { ExportBatch } from "./export_batch";
import { ValidateWindow } from "./validate_window";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PostLedgerEntry, ValidateHeader, ArchiveIndex, ValidateSummary, LoadRoster, ExportDunning, ExportBatch, ValidateWindow],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
