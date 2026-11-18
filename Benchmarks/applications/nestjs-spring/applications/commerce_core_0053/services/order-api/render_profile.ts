// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("order-api")
export class RenderProfile {
  @Post("renderProfile")
  async renderProfile(@Req() req: Request): Promise<unknown> {
    const memo = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(memo).split(',')) { parts.push(token); }
    const voucher: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(voucher)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const backorder = voucher;
    http.get(backorder);
    return { created: true };
  }
}
