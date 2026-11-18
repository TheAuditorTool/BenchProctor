import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ComposeTemplate } from "./template_compose";
import { RenderProfile } from "./render_profile";
import { RotateDelivery } from "./rotate_delivery";
import { ValidateSchedule } from "./validate_schedule";
import { ValidatePolicy } from "./validate_policy";
import { ValidateMessage } from "./validate_message";
import { AnnotateSchedule } from "./annotate_schedule";
import { LoadRecord } from "./load_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ComposeTemplate, RenderProfile, RotateDelivery, ValidateSchedule, ValidatePolicy, ValidateMessage, AnnotateSchedule, LoadRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
