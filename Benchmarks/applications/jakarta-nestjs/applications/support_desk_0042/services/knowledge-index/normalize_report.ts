// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("knowledge-index")
export class NormalizeReport {
  @Post("normalizeReport")
  async normalizeReport(@Req() req: Request): Promise<unknown> {
    const blurb = process.env.SUPPORT_INPUT_0042 || "";
    const transform = (v: string): string => v.trim();
    const inquiry: string = transform(blurb);
    if (!/^(asc|desc|name|created)$/.test(String(inquiry))) { throw new BadRequestException({error:"invalid"}); }
    const grievance = inquiry;
    await db.query("SELECT * FROM users ORDER BY " + grievance);
    return { created: true };
  }
}
