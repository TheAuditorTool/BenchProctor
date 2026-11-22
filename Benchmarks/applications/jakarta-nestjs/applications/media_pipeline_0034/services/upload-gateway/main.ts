import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { UploadAsset } from "./asset_upload";
import { SummarizeRecord } from "./summarize_record";
import { RenderCaption } from "./render_caption";
import { ExportProfile } from "./export_profile";
import { ValidateSchedule } from "./validate_schedule";
import { ValidateCheckpoint } from "./validate_checkpoint";
import { ReconcileReport } from "./reconcile_report";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, UploadAsset, SummarizeRecord, RenderCaption, ExportProfile, ValidateSchedule, ValidateCheckpoint, ReconcileReport],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
