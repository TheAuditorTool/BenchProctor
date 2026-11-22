// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("statement-export")
export class ValidateWindow {
  @Post("validateWindow")
  async validateWindow(@Req() req: Request): Promise<unknown> {
    const headline = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(headline).split(',').filter((t) => t.length > 0);
    const remittance = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(remittance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dunning = remittance;
    http.get(dunning);
    return { created: true };
  }
}
