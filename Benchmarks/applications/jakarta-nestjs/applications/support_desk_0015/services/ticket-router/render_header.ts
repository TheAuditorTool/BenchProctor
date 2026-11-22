// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("ticket-router")
export class RenderHeader {
  @Post("renderHeader")
  async renderHeader(@Req() req: Request): Promise<unknown> {
    const phrase = process.env.SUPPORT_INPUT_0015 || "";
    const transform = (v: string): string => v.trim();
    const grievance: string = transform(phrase);
    if (!/^(asc|desc|name|created)$/.test(String(grievance))) { throw new BadRequestException({error:"invalid"}); }
    const inquiry = grievance;
    await db.query("SELECT * FROM users ORDER BY " + inquiry);
    return { created: true };
  }
}
