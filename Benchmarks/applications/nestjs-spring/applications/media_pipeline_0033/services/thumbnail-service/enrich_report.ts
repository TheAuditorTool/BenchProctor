// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("thumbnail-service")
export class EnrichReport {
  @Post("enrichReport")
  async enrichReport(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const rendition: string = normalize(transcript);
    const resolved = path.resolve("/var/app/data", rendition);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const montage = resolved;
    fs.writeFileSync(montage, "data");
    return { created: true };
  }
}
