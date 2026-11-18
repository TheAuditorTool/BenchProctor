// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("watermark-service")
export class PublishReport {
  @Post("publishReport")
  async publishReport(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.referer as string) || "";
    const tokens = String(tagline).split(',').filter((t) => t.length > 0);
    const rendition = tokens.join(' ');
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(rendition)) { throw new ForbiddenException({error:"forbidden"}); }
    const montage = "/var/app/data/" + rendition;
    fs.unlinkSync(montage);
    return { created: true };
  }
}
