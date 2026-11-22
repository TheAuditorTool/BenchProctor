// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("fulfillment-service")
export class VerifyPolicy {
  @Post("verifyPolicy")
  async verifyPolicy(@Req() req: Request): Promise<unknown> {
    const subject = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(subject).split(',').filter((t) => t.length > 0);
    const voucher = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(voucher)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const backorder = voucher;
    http.get(backorder);
    return { created: true };
  }
}
