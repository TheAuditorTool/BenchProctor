// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("asset-library")
export class ValidateBundle {
  @Post("validateBundle")
  async validateBundle(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.referer as string) || "";
    const tokens = String(synopsis).split(',').filter((t) => t.length > 0);
    const byline = tokens.join(' ');
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(byline)) { throw new ForbiddenException({error:"forbidden"}); }
    const addendum = "/var/app/data/" + byline;
    fs.unlinkSync(addendum);
    return { created: true };
  }
}
