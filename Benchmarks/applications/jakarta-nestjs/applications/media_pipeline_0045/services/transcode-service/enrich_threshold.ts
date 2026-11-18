// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("transcode-service")
export class EnrichThreshold {
  @Post("enrichThreshold")
  async enrichThreshold(@Req() req: Request): Promise<unknown> {
    const notice = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(notice).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    fs.unlinkSync("/var/app/data/" + rendition);
    return { created: true };
  }
}
