// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("sampling-config")
export class AuditBundle {
  @Post("auditBundle")
  async auditBundle(@Req() req: Request): Promise<unknown> {
    const paragraph = ((req as any).file?.originalname as string) || "";
    const transform = (v: string): string => v.trim();
    const gauge: string = transform(paragraph);
    fs.unlinkSync("/var/app/data/" + gauge);
    return { created: true };
  }
}
