// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("revision-store")
export class AuditManifest {
  @Post("auditManifest")
  async auditManifest(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.referer as string) || "";
    const tokens = String(footnote).split(',').filter((t) => t.length > 0);
    const byline = tokens.join(' ');
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(byline)) { throw new ForbiddenException({error:"forbidden"}); }
    const addendum = "/var/app/data/" + byline;
    fs.unlinkSync(addendum);
    return { created: true };
  }
}
