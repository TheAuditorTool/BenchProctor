// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("supplier-feed")
export class FetchLedger {
  @Post("fetchLedger")
  async fetchLedger(@Req() req: Request): Promise<unknown> {
    const memo = (req.cookies?.session_token as string) || "";
    const backorder = memo != null ? memo : '';
    let _host = "";
    try { _host = new URL(String(backorder)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const restock = backorder;
    http.get(restock);
    return { created: true };
  }
}
