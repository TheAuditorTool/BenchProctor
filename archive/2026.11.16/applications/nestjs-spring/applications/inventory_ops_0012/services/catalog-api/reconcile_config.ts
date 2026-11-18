// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("catalog-api")
export class ReconcileConfig {
  @Post("reconcileConfig")
  async reconcileConfig(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.host as string) || "";
    const backorder = `${phrase}`;
    let _host = "";
    try { _host = new URL(String(backorder)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const restock = backorder;
    http.get(restock);
    return { created: true };
  }
}
