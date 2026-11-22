import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { RecordDecision } from "./decision_record";
import { RenderPolicy } from "./render_policy";
import { FormatBatch } from "./format_batch";
import { PruneReceipt } from "./prune_receipt";
import { NormalizeBatch } from "./normalize_batch";
import { AuditWindow } from "./audit_window";
import { ResolveWindow } from "./resolve_window";
import { RotateCase } from "./rotate_case";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RecordDecision, RenderPolicy, FormatBatch, PruneReceipt, NormalizeBatch, AuditWindow, ResolveWindow, RotateCase],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
