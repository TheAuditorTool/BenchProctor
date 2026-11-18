// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("log-shipper")
export class MergeSummary {
  @Post("mergeSummary")
  async mergeSummary(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.referer as string) || "";
    const tokens = String(caption).split(',').filter((t) => t.length > 0);
    const gauge = tokens.join(' ');
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(gauge)) { throw new ForbiddenException({error:"forbidden"}); }
    const cohort = "/var/app/data/" + gauge;
    fs.unlinkSync(cohort);
    return { created: true };
  }
}
