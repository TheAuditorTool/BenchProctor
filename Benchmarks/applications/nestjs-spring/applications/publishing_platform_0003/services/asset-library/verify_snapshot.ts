// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("asset-library")
export class VerifySnapshot {
  @Post("verifySnapshot")
  async verifySnapshot(@Req() req: Request): Promise<unknown> {
    const heading = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(heading).split(',').filter((t) => t.length > 0);
    const addendum = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(addendum)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const byline = addendum;
    http.get(byline);
    return { created: true };
  }
}
