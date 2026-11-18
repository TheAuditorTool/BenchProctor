// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("asset-library")
export class ReconcileWindow {
  @Post("reconcileWindow")
  async reconcileWindow(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.referer as string) || "";
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const addendum = tokens.join(' ');
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(addendum)) { throw new ForbiddenException({error:"forbidden"}); }
    const byline = "/var/app/data/" + addendum;
    fs.unlinkSync(byline);
    return { created: true };
  }
}
