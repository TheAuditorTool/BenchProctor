import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { CapturePayment } from "./payment_capture";
import { CompactPolicy } from "./compact_policy";
import { PublishInvoice } from "./publish_invoice";
import { ValidateReceipt } from "./validate_receipt";
import { FetchInvoice } from "./fetch_invoice";
import { RotateSnapshot } from "./rotate_snapshot";
import { NormalizePolicy } from "./normalize_policy";
import { SummarizeProfile } from "./summarize_profile";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, CapturePayment, CompactPolicy, PublishInvoice, ValidateReceipt, FetchInvoice, RotateSnapshot, NormalizePolicy, SummarizeProfile],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
