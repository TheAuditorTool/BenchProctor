import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { IssueRefund } from "./refund_issue";
import { AuditBundle } from "./audit_bundle";
import { ExportSummary } from "./export_summary";
import { ExportHeader } from "./export_header";
import { FormatStatement } from "./format_statement";
import { CompactDunning } from "./compact_dunning";
import { CompactDigest } from "./compact_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, IssueRefund, AuditBundle, ExportSummary, ExportHeader, FormatStatement, CompactDunning, CompactDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
