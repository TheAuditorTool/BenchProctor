// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("catalog-api")
export class LoadBatch {
  @Post("loadBatch")
  async loadBatch(@Req() req: Request): Promise<unknown> {
    const excerpt = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(excerpt).split(',').filter((t) => t.length > 0);
    const restock = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(restock)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const backorder = restock;
    http.get(backorder);
    return { created: true };
  }
}
