import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { StoreArchive } from "./archive_store";
import { SummarizeManifest } from "./summarize_manifest";
import { FormatRedaction } from "./format_redaction";
import { LoadBundle } from "./load_bundle";
import { ResolveBundle } from "./resolve_bundle";
import { RotateCheckpoint } from "./rotate_checkpoint";
import { ArchiveBundle } from "./archive_bundle";
import { MergeLedger } from "./merge_ledger";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, StoreArchive, SummarizeManifest, FormatRedaction, LoadBundle, ResolveBundle, RotateCheckpoint, ArchiveBundle, MergeLedger],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
