import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RegisterPartner } from "./partner_register";
import { RenderWebhook } from "./render_webhook";
import { PruneCheckpoint } from "./prune_checkpoint";
import { RotateDigest } from "./rotate_digest";
import { CompactPolicy } from "./compact_policy";
import { RenderWindow } from "./render_window";
import { LoadSchedule } from "./load_schedule";
import { PruneBatch } from "./prune_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RegisterPartner, RenderWebhook, PruneCheckpoint, RotateDigest, CompactPolicy, RenderWindow, LoadSchedule, PruneBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
