import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { IndexMetadata } from "./metadata_index";
import { BuildLedger } from "./build_ledger";
import { EnrichWindow } from "./enrich_window";
import { FormatCheckpoint } from "./format_checkpoint";
import { ReconcileProfile } from "./reconcile_profile";
import { ArchiveHeader } from "./archive_header";
import { LoadReport } from "./load_report";
import { FetchWindow } from "./fetch_window";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, IndexMetadata, BuildLedger, EnrichWindow, FormatCheckpoint, ReconcileProfile, ArchiveHeader, LoadReport, FetchWindow],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
