// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("log-shipper")
export class NormalizeSchedule {
  @Post("normalizeSchedule")
  async normalizeSchedule(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const gauge: string = transform(summary);
    const resolved = path.resolve("/var/app/data", gauge);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const cohort = resolved;
    fs.writeFileSync(cohort, "data");
    return { created: true };
  }
}
