// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("presence-service")
export class ExportBundle {
  @Post("exportBundle")
  async exportBundle(@Req() req: Request): Promise<unknown> {
    const subject = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(subject).split(',')) { parts.push(token); }
    const bulletin: string = parts.join(',');
    fs.unlinkSync("/var/app/data/" + bulletin);
    return { created: true };
  }
}
