// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("macro-service")
export class ResolveIndex {
  @Post("resolveIndex")
  async resolveIndex(@Req() req: Request): Promise<unknown> {
    const preface = process.env.SUPPORT_INPUT_0051 || "";
    const transform = (v: string): string => v.trim();
    const grievance: string = transform(preface);
    if (!/^(asc|desc|name|created)$/.test(String(grievance))) { throw new BadRequestException({error:"invalid"}); }
    const inquiry = grievance;
    await db.query("SELECT * FROM users ORDER BY " + inquiry);
    return { created: true };
  }
}
