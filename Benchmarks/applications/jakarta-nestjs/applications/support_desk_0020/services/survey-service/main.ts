import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SendSurvey } from "./survey_send";
import { RenderTicket } from "./render_ticket";
import { LoadBundle } from "./load_bundle";
import { ArchiveConfig } from "./archive_config";
import { ArchiveSnapshot } from "./archive_snapshot";
import { ValidateWindow } from "./validate_window";
import { ValidateBundle } from "./validate_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SendSurvey, RenderTicket, LoadBundle, ArchiveConfig, ArchiveSnapshot, ValidateWindow, ValidateBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
