// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("metadata-index")
export class ResolveReceipt {
  @Post("resolveReceipt")
  async resolveReceipt(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    const rendition = Buffer.from(citation, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(rendition)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const montage = rendition;
    http.get(montage);
    return { created: true };
  }
}
