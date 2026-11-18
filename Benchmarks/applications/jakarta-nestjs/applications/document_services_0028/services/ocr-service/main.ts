import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ExtractText } from "./ocr_extract";
import { PublishCheckpoint } from "./publish_checkpoint";
import { AnnotateSchedule } from "./annotate_schedule";
import { CompactHeader } from "./compact_header";
import { RenderConversion } from "./render_conversion";
import { RenderAttachment } from "./render_attachment";
import { NormalizeConfig } from "./normalize_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ExtractText, PublishCheckpoint, AnnotateSchedule, CompactHeader, RenderConversion, RenderAttachment, NormalizeConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
