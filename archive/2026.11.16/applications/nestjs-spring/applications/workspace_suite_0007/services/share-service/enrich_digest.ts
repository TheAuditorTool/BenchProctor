// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("share-service")
export class EnrichDigest {
  @Post("enrichDigest")
  async enrichDigest(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.host as string) || "";
    const subtitle = `${summary}`;
    let _host = "";
    try { _host = new URL(String(subtitle)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const notice = subtitle;
    http.get(notice);
    return { created: true };
  }
}
