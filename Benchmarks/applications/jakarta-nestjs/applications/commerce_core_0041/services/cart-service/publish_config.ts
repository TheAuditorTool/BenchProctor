// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("cart-service")
export class PublishConfig {
  @Post("publishConfig")
  async publishConfig(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers["user-agent"] as string) || "";
    let _host = "";
    try { _host = new URL(String(headline)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const voucher = headline;
    http.get(voucher);
    return { created: true };
  }
}
