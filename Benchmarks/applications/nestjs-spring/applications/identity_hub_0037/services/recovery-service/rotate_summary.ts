// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("recovery-service")
export class RotateSummary {
  @Post("rotateSummary")
  async rotateSummary(@Req() req: Request): Promise<unknown> {
    const remark = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(remark).split(',').filter((t) => t.length > 0);
    const persona = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const notice = persona;
    http.get(notice);
    return { created: true };
  }
}
