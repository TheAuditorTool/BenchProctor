// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("promo-service")
export class FetchSummary {
  @Post("fetchSummary")
  async fetchSummary(@Req() req: Request): Promise<unknown> {
    const heading = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(heading).split(',')) { parts.push(token); }
    const voucher: string = parts.join(',');
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(voucher));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const backorder = _parsed.data;
    childProcess.execSync("echo " + backorder);
    return { created: true };
  }
}
