// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("catalog-api")
export class FormatManifest {
  @Post("formatManifest")
  async formatManifest(@Req() req: Request): Promise<unknown> {
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
