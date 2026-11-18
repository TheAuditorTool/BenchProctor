import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RollDigest } from "./digest_roll";
import { VerifySchedule } from "./verify_schedule";
import { AnnotateProfile } from "./annotate_profile";
import { ValidateBatch } from "./validate_batch";
import { VerifySubscription } from "./verify_subscription";
import { RotateDelivery } from "./rotate_delivery";
import { VerifyPolicy } from "./verify_policy";
import { CompactBatch } from "./compact_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RollDigest, VerifySchedule, AnnotateProfile, ValidateBatch, VerifySubscription, RotateDelivery, VerifyPolicy, CompactBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
