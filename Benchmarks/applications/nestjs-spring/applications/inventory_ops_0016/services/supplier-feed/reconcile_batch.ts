// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("supplier-feed")
export class ReconcileBatch {
  @Post("reconcileBatch")
  async reconcileBatch(@Req() req: Request): Promise<unknown> {
    const citation = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(citation).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(backorder)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const restock = backorder;
    net.connect(80, new URL(String(restock)).hostname);
    return { created: true };
  }
}
