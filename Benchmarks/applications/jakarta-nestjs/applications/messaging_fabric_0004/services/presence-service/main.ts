import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { UpdatePresence } from "./presence_update";
import { EnrichSummary } from "./enrich_summary";
import { LoadReceipt } from "./load_receipt";
import { EnrichReceipt } from "./enrich_receipt";
import { ValidateReport } from "./validate_report";
import { ExportConfig } from "./export_config";
import { AnnotateSnapshot } from "./annotate_snapshot";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, UpdatePresence, EnrichSummary, LoadReceipt, EnrichReceipt, ValidateReport, ExportConfig, AnnotateSnapshot],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
