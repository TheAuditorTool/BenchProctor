// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("escalation-service")
export class PublishThreshold {
  @Post("publishThreshold")
  async publishThreshold(@Req() req: Request): Promise<unknown> {
    const snippet = ((req as any).file?.originalname as string) || "";
    const transform = (v: string): string => v.trim();
    const inquiry: string = transform(snippet);
    fs.unlinkSync("/var/app/data/" + inquiry);
    return { created: true };
  }
}
