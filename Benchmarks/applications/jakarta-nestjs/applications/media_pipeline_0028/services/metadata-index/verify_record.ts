// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("metadata-index")
export class VerifyRecord {
  @Post("verifyRecord")
  async verifyRecord(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    const payload = { get value() { return citation; } };
    const rendition = payload.value;
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(rendition)) { throw new ForbiddenException({error:"forbidden"}); }
    const montage = "/var/app/data/" + rendition;
    fs.writeFileSync(montage, "data");
    return { created: true };
  }
}
