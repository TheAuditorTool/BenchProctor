// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("thumbnail-service")
export class LoadLedger {
  @Post("loadLedger")
  async loadLedger(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const rendition: string = transform(transcript);
    const resolved = path.resolve("/var/app/data", rendition);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const montage = resolved;
    fs.writeFileSync(montage, "data");
    return { created: true };
  }
}
