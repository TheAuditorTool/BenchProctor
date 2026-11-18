// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("anomaly-scorer")
export class FormatDigest {
  @Post("formatDigest")
  async formatDigest(@Req() req: Request): Promise<unknown> {
    const summary = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const transform = (v: string): string => v.trim();
    const gauge: string = transform(summary);
    const resolved = path.resolve("/var/app/data", gauge);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const cohort = resolved;
    const fileContent = fs.readFileSync(cohort, "utf8");
    return fileContent;
  }
}
