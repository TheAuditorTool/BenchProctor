import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { InvokeConnector } from "./connector_invoke";
import { ValidateWebhook } from "./validate_webhook";
import { FormatHeader } from "./format_header";
import { ReconcileSnapshot } from "./reconcile_snapshot";
import { ExportWindow } from "./export_window";
import { ExportPolicy } from "./export_policy";
import { SummarizeBatch } from "./summarize_batch";
import { RenderConfig } from "./render_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, InvokeConnector, ValidateWebhook, FormatHeader, ReconcileSnapshot, ExportWindow, ExportPolicy, SummarizeBatch, RenderConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
