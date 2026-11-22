import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PostComment } from "./comment_post";
import { ReconcileManifest } from "./reconcile_manifest";
import { ReconcileComment } from "./reconcile_comment";
import { CompactManifest } from "./compact_manifest";
import { LoadReceipt } from "./load_receipt";
import { AnnotateLedger } from "./annotate_ledger";
import { ArchiveSnapshot } from "./archive_snapshot";
import { FormatRecord } from "./format_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PostComment, ReconcileManifest, ReconcileComment, CompactManifest, LoadReceipt, AnnotateLedger, ArchiveSnapshot, FormatRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
