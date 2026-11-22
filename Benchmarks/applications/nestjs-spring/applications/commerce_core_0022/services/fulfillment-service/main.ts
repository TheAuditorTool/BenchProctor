import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { QueueFulfillment } from "./fulfillment_queue";
import { NormalizePromotion } from "./normalize_promotion";
import { CompactSummary } from "./compact_summary";
import { VerifyPolicy } from "./verify_policy";
import { FormatCart } from "./format_cart";
import { CompactConfig } from "./compact_config";
import { ExportReport } from "./export_report";
import { ValidateManifest } from "./validate_manifest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QueueFulfillment, NormalizePromotion, CompactSummary, VerifyPolicy, FormatCart, CompactConfig, ExportReport, ValidateManifest],
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
