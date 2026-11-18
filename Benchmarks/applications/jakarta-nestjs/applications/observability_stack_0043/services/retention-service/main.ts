import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SweepRetention } from "./retention_sweep";
import { SummarizeAlert } from "./summarize_alert";
import { ExportRoster } from "./export_roster";
import { VerifyThreshold } from "./verify_threshold";
import { ValidateRecord } from "./validate_record";
import { PruneCheckpoint } from "./prune_checkpoint";
import { ExportHeader } from "./export_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SweepRetention, SummarizeAlert, ExportRoster, VerifyThreshold, ValidateRecord, PruneCheckpoint, ExportHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
