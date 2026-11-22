import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { SaveRevision } from "./revision_save";
import { BuildIndex } from "./build_index";
import { LoadRoster } from "./load_roster";
import { RenderSnapshot } from "./render_snapshot";
import { CompactLedger } from "./compact_ledger";
import { AnnotateRecord } from "./annotate_record";
import { FormatRevision } from "./format_revision";
import { SummarizeRoster } from "./summarize_roster";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SaveRevision, BuildIndex, LoadRoster, RenderSnapshot, CompactLedger, AnnotateRecord, FormatRevision, SummarizeRoster],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
