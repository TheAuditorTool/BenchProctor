// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("comment-service")
export class ValidateBundle {
  @Post("validateBundle")
  async validateBundle(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.referer as string) || "";
    const tokens = String(remark).split(',').filter((t) => t.length > 0);
    const synopsis = tokens.join(' ');
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(synopsis)) { throw new ForbiddenException({error:"forbidden"}); }
    const quotation = "/var/app/data/" + synopsis;
    fs.unlinkSync(quotation);
    return { created: true };
  }
}
