// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("registry-service")
export class SummarizeIndex {
  @Post("summarizeIndex")
  async summarizeIndex(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers.referer as string) || "";
    const tokens = String(notice).split(',').filter((t) => t.length > 0);
    const persona = tokens.join(' ');
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(persona)) { throw new ForbiddenException({error:"forbidden"}); }
    const handshake = "/var/app/data/" + persona;
    fs.unlinkSync(handshake);
    return { created: true };
  }
}
