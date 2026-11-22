import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { IndexDocument } from "./search_index";
import { RotateConversion } from "./rotate_conversion";
import { RotateSchedule } from "./rotate_schedule";
import { ArchiveSignature } from "./archive_signature";
import { BuildRoster } from "./build_roster";
import { ReconcileWindow } from "./reconcile_window";
import { BuildThreshold } from "./build_threshold";
import { RenderConversion } from "./render_conversion";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, IndexDocument, RotateConversion, RotateSchedule, ArchiveSignature, BuildRoster, ReconcileWindow, BuildThreshold, RenderConversion],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
