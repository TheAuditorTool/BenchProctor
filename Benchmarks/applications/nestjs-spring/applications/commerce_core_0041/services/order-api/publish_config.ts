// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("order-api")
export class PublishConfig {
  @Post("publishConfig")
  async publishConfig(@Req() req: Request): Promise<unknown> {
    const headline = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(headline).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(backorder)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const voucher = backorder;
    http.get(voucher);
    return { created: true };
  }
}
