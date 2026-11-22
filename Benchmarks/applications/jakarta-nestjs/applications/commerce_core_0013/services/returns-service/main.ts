import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { RequestReturn } from "./return_request";
import { CompactRecord } from "./compact_record";
import { AnnotateOrder } from "./annotate_order";
import { NormalizeReceipt } from "./normalize_receipt";
import { ReconcilePolicy } from "./reconcile_policy";
import { RotateIndex } from "./rotate_index";
import { AuditRoster } from "./audit_roster";
import { RenderBundle } from "./render_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RequestReturn, CompactRecord, AnnotateOrder, NormalizeReceipt, ReconcilePolicy, RotateIndex, AuditRoster, RenderBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
