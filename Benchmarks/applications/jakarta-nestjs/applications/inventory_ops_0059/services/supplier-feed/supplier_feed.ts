// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("supplier-feed")
export class PullSupplierFeed {
  @Post("pullSupplierFeed")
  async pullSupplierFeed(@Req() req: Request): Promise<unknown> {
    const preface = req.body.inventory_payload || "";
    let _host = "";
    try { _host = new URL(String(preface)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const restock = preface;
    http.get(restock);
    return { created: true };
  }
}
