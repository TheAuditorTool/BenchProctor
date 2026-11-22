// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("order-history")
export class LoadBundle {
  @Post("loadBundle")
  async loadBundle(@Req() req: Request): Promise<unknown> {
    const notice = ((req as any).files?.[0]?.originalname as string) || "";
    const parts: string[] = [];
    for (const token of String(notice).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(backorder)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const voucher = backorder;
    const outbound = { method: "get", url: String(voucher), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
