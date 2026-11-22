// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("retry-service")
export class PublishSummary {
  @Post("publishSummary")
  async publishSummary(@Req() req: Request): Promise<unknown> {
    const summary = ((req as any).file?.originalname as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(summary);
    fs.unlinkSync("/var/app/data/" + handshake);
    return { created: true };
  }
}
