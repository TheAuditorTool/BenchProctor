import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { MapField } from "./field_mapping";
import { SummarizeHeader } from "./summarize_header";
import { ValidateMapping } from "./validate_mapping";
import { FormatHeader } from "./format_header";
import { ReconcileSnapshot } from "./reconcile_snapshot";
import { ExportWindow } from "./export_window";
import { ExportPolicy } from "./export_policy";
import { SummarizeBatch } from "./summarize_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, MapField, SummarizeHeader, ValidateMapping, FormatHeader, ReconcileSnapshot, ExportWindow, ExportPolicy, SummarizeBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
