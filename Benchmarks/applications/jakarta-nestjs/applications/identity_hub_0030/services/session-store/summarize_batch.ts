// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("session-store")
export class SummarizeBatch {
  @Post("summarizeBatch")
  async summarizeBatch(@Req() req: Request): Promise<unknown> {
    const tagline = (req.body as string) || "";
    const payload = { get value() { return tagline; } };
    const persona = payload.value;
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(persona)) { throw new ForbiddenException({error:"forbidden"}); }
    const note = "/var/app/data/" + persona;
    fs.writeFileSync(note, "data");
    return { created: true };
  }
}
