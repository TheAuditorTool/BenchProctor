import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { ConfigureSample } from "./sample_config";
import { AuditBundle } from "./audit_bundle";
import { CollectCheckpoint } from "./collect_checkpoint";
import { RenderSchedule } from "./render_schedule";
import { LoadMetric } from "./load_metric";
import { EnrichRoster } from "./enrich_roster";
import { ExportHeader } from "./export_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ConfigureSample, AuditBundle, CollectCheckpoint, RenderSchedule, LoadMetric, EnrichRoster, ExportHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
