// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("quota-service")
export class SummarizeWindow {
  @Post("summarizeWindow")
  async summarizeWindow(@Req() req: Request): Promise<unknown> {
    const remark = process.env.PLATFORM_INPUT_0032 || "";
    const transform = (v: string): string => v.trim();
    const persona: string = transform(remark);
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    await db.query("SELECT * FROM users ORDER BY " + handshake);
    return { created: true };
  }
}
