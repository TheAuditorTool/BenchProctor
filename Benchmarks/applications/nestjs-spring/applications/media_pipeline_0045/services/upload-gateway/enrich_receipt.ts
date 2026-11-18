// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("upload-gateway")
export class EnrichReceipt {
  @Post("enrichReceipt")
  async enrichReceipt(@Req() req: Request): Promise<unknown> {
    const notice = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(notice).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(rendition)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const montage = rendition;
    http.get(montage);
    return { created: true };
  }
}
