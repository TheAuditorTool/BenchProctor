// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("preview-renderer")
export class ArchiveRecord {
  @Post("archiveRecord")
  async archiveRecord(@Req() req: Request): Promise<unknown> {
    const remark = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(remark).split(',').filter((t) => t.length > 0);
    const byline = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(byline)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const addendum = byline;
    http.get(addendum);
    return { created: true };
  }
}
